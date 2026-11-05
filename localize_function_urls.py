"""Русские адреса функций и трёхъязычный переключатель EN/RU/DE для MkDocs.

Исходные .md и nav остаются неизменными: это важно для mkdocs-static-i18n
с docs_structure=suffix. После mkdocs build переносим только готовые HTML
и корректируем ссылки/поисковый индекс. Таблица соответствий берётся из
mkdocs.yml -> plugins -> i18n -> ru -> nav_translations.
"""

from __future__ import annotations

from html import escape, unescape
import gzip
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

import yaml

BASE_URL = "https://help.kombinator.net"
FUNCTIONS_PREFIX = "ReferenceGuide/functions/"
HTML_URL_ATTR = re.compile(r'(?P<start>\b(?:href|action)\s*=\s*)(?P<quote>["\'])(?P<url>[^"\']*)(?P=quote)', re.I | re.S)
META_REFRESH = re.compile(r'(?P<start>\bcontent\s*=\s*)(?P<quote>["\'])(?P<delay>\d+\s*;\s*url\s*=\s*)(?P<url>[^"\']*)(?P=quote)', re.I | re.S)


def read_function_mapping(config_file: Path) -> dict[str, str]:
    """Вернуть { 'ReferenceGuide/functions/Math/round/': '.../округлить/' }."""
    config = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    i18n = next(plugin["i18n"] for plugin in config["plugins"] if isinstance(plugin, dict) and "i18n" in plugin)
    ru = next(lang for lang in i18n["languages"] if lang["locale"] == "ru")
    translations = ru["nav_translations"]
    functions = next(item["Function"] for item in config["nav"] if "Function" in item)
    mapping = {}
    target_paths = set()

    for group in functions:
        for entries in group.values():
            for entry in entries:
                for english_name, md_path in entry.items():
                    source = Path(md_path)
                    if not md_path.startswith(FUNCTIONS_PREFIX) or source.suffix != ".md":
                        raise ValueError(f"Неожиданный путь функции: {md_path}")
                    if english_name not in translations:
                        raise ValueError(f"Нет русского названия для {english_name} в nav_translations")
                    russian_name = str(translations[english_name]).strip()
                    if not russian_name or russian_name in (".", "..") or "/" in russian_name or "\\" in russian_name:
                        raise ValueError(f"Недопустимое русское имя функции: {english_name} -> {russian_name}")
                    # MkDocs обрабатывает index.md как индекс каталога:
                    # Lists/index.md -> /Lists/, а не /Lists/index/.
                    old = (source.parent.as_posix() + "/") if source.stem == "index" else (source.with_suffix("").as_posix() + "/")
                    new = source.parent.as_posix() + "/" + russian_name + "/"
                    if new in target_paths:
                        raise ValueError(f"Дублирующийся русский адрес функции: {new}")
                    target_paths.add(new)
                    if old != new:
                        mapping[old] = new

    return mapping


def rewrite_site_path(path: str, mapping: dict[str, str]) -> str:
    """Заменить только адреса русских функций, оставив другие пути без изменений."""
    # urlsplit отдаёт percent-encoded path без декодирования.
    decoded = unquote(path)
    prefix = "/ru/"
    if not decoded.startswith(prefix):
        return path
    relative = decoded[len(prefix):]
    for old, new in mapping.items():
        if relative in (old, old.rstrip("/")):
            return prefix + new
        if relative == old + "index.html":
            return prefix + new + "index.html"
    return path


def rewrite_link(raw_url: str, page_url: str, mapping: dict[str, str]) -> str:
    """Перевести ссылку на русскую функцию, корректно разрешая ../ и #."""
    decoded_url = unescape(raw_url)
    if not decoded_url or decoded_url.startswith(("#", "?", "mailto:", "tel:", "javascript:", "data:")):
        return raw_url
    absolute = urljoin(BASE_URL + page_url, decoded_url)
    parts = urlsplit(absolute)
    if parts.netloc != urlsplit(BASE_URL).netloc:
        return raw_url
    new_path = rewrite_site_path(parts.path, mapping)
    if new_path == parts.path:
        return raw_url
    original = urlsplit(decoded_url)
    if original.scheme in ("https", "http") and original.netloc:
        result = urlunsplit((original.scheme, original.netloc, new_path, parts.query, parts.fragment))
    elif decoded_url.startswith("//"):
        result = urlunsplit(("", original.netloc, new_path, parts.query, parts.fragment))
    else:
        result = urlunsplit(("", "", new_path, parts.query, parts.fragment))
    return escape(result, quote=True)


def rewrite_html_links(site: Path, mapping: dict[str, str]) -> tuple[int, int]:
    modified_pages = modified_links = 0
    for html_file in site.rglob("*.html"):
        relative = html_file.relative_to(site)
        page_url = "/" + relative.parent.as_posix().strip(".") + "/"
        # Для корня сайта не создаём двойную косую черту.
        page_url = re.sub(r"/{2,}", "/", page_url)
        original = html_file.read_text(encoding="utf-8")
        replacements = 0

        def rewrite_attr(match: re.Match[str]) -> str:
            nonlocal replacements
            old = match.group("url")
            new = rewrite_link(old, page_url, mapping)
            if new != old:
                replacements += 1
                return match.group("start") + match.group("quote") + new + match.group("quote")
            return match.group(0)

        changed = HTML_URL_ATTR.sub(rewrite_attr, original)

        def rewrite_refresh(match: re.Match[str]) -> str:
            nonlocal replacements
            old = match.group("url")
            new = rewrite_link(old, page_url, mapping)
            if new != old:
                replacements += 1
                return match.group("start") + match.group("quote") + match.group("delay") + new + match.group("quote")
            return match.group(0)

        changed = META_REFRESH.sub(rewrite_refresh, changed)
        if changed != original:
            html_file.write_text(changed, encoding="utf-8")
            modified_pages += 1
            modified_links += replacements
    return modified_pages, modified_links


def rewrite_search_indices(site: Path, mapping: dict[str, str]) -> tuple[int, int]:
    files = entries = 0
    for search_index in site.rglob("search_index.json"):
        data = json.loads(search_index.read_text(encoding="utf-8"))
        changed = False
        for item in data.get("docs", []):
            old = item.get("location", "")
            # search_index.json использует URL относительно корня сайта.
            parts = urlsplit("/" + old.lstrip("/"))
            new_path = rewrite_site_path(parts.path, mapping)
            if new_path != parts.path:
                item["location"] = urlunsplit(("", "", new_path.lstrip("/"), parts.query, parts.fragment))
                entries += 1
                changed = True
        if changed:
            search_index.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
            files += 1
    return files, entries


def redirect_html(target_url: str, lang: str = "ru") -> str:
    safe_url = escape(target_url, quote=True)
    js_url = json.dumps(target_url, ensure_ascii=False)
    return (f"<!doctype html><html lang=\"{lang}\"><head><meta charset=\"utf-8\">"
            f'<meta http-equiv="refresh" content="0;url={safe_url}">'
            f'<link rel="canonical" href="{safe_url}">'
            f'<script>location.replace({js_url} + location.search + location.hash);</script>'
            '</head><body>'
            f'<a href="{safe_url}">Перейти к статье</a>'
            '</body></html>')



def normalize_index_article_links(html_text: str, old_url: str, new_url: str) -> str:
    """index.md имеет адрес каталога; после переноса на уровень глубже
    все относительные ссылки и настройки Material должны остаться рабочими.
    """
    attr_re = re.compile(r'(?P<start>\b(?:href|src|action)\s*=\s*)(?P<quote>["\'])(?P<url>[^"\']*)(?P=quote)', re.I | re.S)

    def absolute_attr(match: re.Match[str]) -> str:
        value = unescape(match.group("url"))
        if not value or value.startswith(("#", "?", "mailto:", "tel:", "javascript:", "data:")):
            return match.group(0)
        if value in ("./", "."):
            new_value = new_url
        else:
            resolved = urlsplit(urljoin(BASE_URL + old_url, value))
            if resolved.netloc != urlsplit(BASE_URL).netloc:
                return match.group(0)
            new_value = urlunsplit(("", "", resolved.path, resolved.query, resolved.fragment))
        return match.group("start") + match.group("quote") + escape(new_value, quote=True) + match.group("quote")

    html_text = attr_re.sub(absolute_attr, html_text)
    # Скрипт Material определяет базовый URL относительно location, а не <base>.
    html_text = re.sub(r'__md_scope=new URL\("[^"\n]*",location\)',
                       '__md_scope=new URL("/",location)', html_text)

    config_re = re.compile(r'(<script id="__config" type="application/json">)(.*?)(</script>)', re.S)

    def fix_config(match: re.Match[str]) -> str:
        data = json.loads(match.group(2))
        for key in ("base", "search"):
            value = data.get(key)
            if isinstance(value, str):
                resolved = urlsplit(urljoin(BASE_URL + old_url, value))
                if resolved.netloc == urlsplit(BASE_URL).netloc:
                    data[key] = resolved.path
        return match.group(1) + json.dumps(data, ensure_ascii=False) + match.group(3)

    return config_re.sub(fix_config, html_text)

def move_russian_pages(site: Path, mapping: dict[str, str]) -> int:
    moved = 0
    for old, new in mapping.items():
        source = site / "ru" / old / "index.html"
        target = site / "ru" / new / "index.html"
        if target.exists():
            raise FileExistsError(f"Целевой адрес уже занят: {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
        if not source.exists():
            # Перевод отсутствует: оба русских URL ведут на английскую статью.
            source.parent.mkdir(parents=True, exist_ok=True)
            fallback = redirect_html("/en/" + old)
            target.write_text(fallback, encoding="utf-8")
            source.write_text(fallback, encoding="utf-8")
            moved += 1
            continue
        if len(Path(new).parts) != len(Path(old).parts):
            # Особенность MkDocs: index.md становится индексом папки.
            # Такой перенос увеличивает глубину URL на один сегмент.
            content = normalize_index_article_links(
                source.read_text(encoding="utf-8"), "/ru/" + old, "/ru/" + new
            )
            target.write_text(content, encoding="utf-8")
        else:
            target.write_bytes(source.read_bytes())
        source.write_text(redirect_html("/ru/" + new), encoding="utf-8")
        moved += 1
    return moved




def read_all_function_routes(config_file: Path) -> dict[str, dict[str, str]]:
    """Все функции: стабильный путь EN, локализованный RU, стабильный DE.

    В немецкой версии пока нет отдельных немецких имён файлов: mkdocs-static-i18n
    использует тот же slug, что в английской. Если перевода нет, build_languages.py
    уже создаёт /de/.../ -> /en/.../ для ТОЙ ЖЕ функции.
    """
    config = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    i18n = next(p["i18n"] for p in config["plugins"] if isinstance(p, dict) and "i18n" in p)
    ru = next(lang for lang in i18n["languages"] if lang["locale"] == "ru")
    translations = ru["nav_translations"]
    functions = next(item["Function"] for item in config["nav"] if "Function" in item)
    routes: dict[str, dict[str, str]] = {}

    for group in functions:
        for entries in group.values():
            for entry in entries:
                for name, md_path in entry.items():
                    source = Path(md_path)
                    if not md_path.startswith(FUNCTIONS_PREFIX) or source.suffix != ".md":
                        raise ValueError(f"Неожиданный путь функции: {md_path}")
                    if name not in translations:
                        raise ValueError(f"Нет русского названия функции: {name}")
                    russian_name = str(translations[name]).strip()
                    if not russian_name or russian_name in (".", "..") or "/" in russian_name or "\\" in russian_name:
                        raise ValueError(f"Недопустимое русское имя функции: {name} -> {russian_name}")
                    # index.md в MkDocs означает адрес папки, а не /index/.
                    english_path = (
                        source.parent.as_posix() + "/"
                        if source.stem == "index"
                        else source.with_suffix("").as_posix() + "/"
                    )
                    russian_path = source.parent.as_posix() + "/" + russian_name + "/"
                    routes[english_path] = {
                        "en": english_path,
                        "ru": russian_path,
                        "de": english_path,
                    }
    return routes


def create_reverse_language_aliases(site: Path, mapping: dict[str, str]) -> int:
    """Подстраховка от ссылок, которые меняют только языковой префикс.

    /en/.../округлить/ -> /en/.../round/
    /de/.../округлить/ -> /de/.../round/

    Основной переключатель всё равно должен указывать сразу на правильный URL.
    Алиасы нужны, чтобы старая ссылка не выдавала 404.
    """
    created = 0
    for old, new in mapping.items():
        for lang in ("en", "de"):
            alias = site / lang / new / "index.html"
            target = site / lang / old / "index.html"
            if not target.is_file():
                raise FileNotFoundError(f"Нет целевой страницы для алиаса: {target}")
            if alias.exists():
                # Не перезаписываем настоящие страницы.
                raise FileExistsError(f"Адрес алиаса занят: {alias}")
            alias.parent.mkdir(parents=True, exist_ok=True)
            alias.write_text(redirect_html("/" + lang + "/" + old, lang=lang), encoding="utf-8")
            created += 1
    return created


def fix_function_language_switcher(site: Path, config_file: Path) -> tuple[int, int]:
    """Исправить переходы EN <-> RU <-> DE на всех страницах функций.

    Любой язык -> EN: английский slug; -> RU: русский slug;
    -> DE: английский slug под /de/ (немецкие .md пока без отдельных имён).
    Если немецкого перевода нет, /de/ страница переадресует на EN той же функции.
    """
    routes = read_all_function_routes(config_file)
    language_link = re.compile(
        r'(?P<start><a\b[^>]*?\bhref\s*=\s*)(?P<quote>["\'])(?P<url>[^"\']*)(?P=quote)'
        r'(?P<middle>[^>]*?\bhreflang\s*=\s*)(?P<langquote>["\'])(?P<lang>en|ru|de)(?P=langquote)',
        re.I | re.S,
    )
    changed_pages = changed_links = 0

    for route in routes.values():
        for current_language in ("en", "ru", "de"):
            page = site / current_language / route[current_language] / "index.html"
            if not page.is_file():
                continue
            original = page.read_text(encoding="utf-8")
            counter = 0

            def replace(match: re.Match[str]) -> str:
                nonlocal counter
                target_language = match.group("lang").lower()
                correct_url = "/" + target_language + "/" + route[target_language]
                if unescape(match.group("url")) == correct_url:
                    return match.group(0)
                counter += 1
                return (
                    match.group("start") + match.group("quote")
                    + escape(correct_url, quote=True)
                    + match.group("quote") + match.group("middle")
                    + match.group("langquote") + match.group("lang")
                    + match.group("langquote")
                )

            updated = language_link.sub(replace, original)
            if updated != original:
                page.write_text(updated, encoding="utf-8")
                changed_pages += 1
                changed_links += counter

    return changed_pages, changed_links


def validate_function_language_switcher(site: Path, config_file: Path) -> None:
    """Проверить, что каждая функция ведёт на ту же функцию в EN, RU и DE."""
    routes = read_all_function_routes(config_file)
    language_link = re.compile(
        r'<a\b[^>]*?\bhref\s*=\s*["\'](?P<url>[^"\']*)["\']'
        r'[^>]*?\bhreflang\s*=\s*["\'](?P<lang>en|ru|de)["\']',
        re.I | re.S,
    )
    for route in routes.values():
        for current_language in ("en", "ru", "de"):
            page = site / current_language / route[current_language] / "index.html"
            if not page.is_file():
                raise FileNotFoundError(f"Нет страницы функции: {page}")
            html_text = page.read_text(encoding="utf-8")
            links = {m.group("lang").lower(): unescape(m.group("url"))
                     for m in language_link.finditer(html_text)}
            if not links:
                # Страница без перевода содержит редирект, а не переключатель.
                # Проверяем, что она ведёт на английскую версию той же функции.
                if 'http-equiv="refresh"' not in html_text or "/en/" + route["en"] not in html_text:
                    raise ValueError(f"Нет переключателя или корректного fallback: {page}")
                continue
            if set(links) != {"en", "ru", "de"}:
                raise ValueError(f"Неполный переключатель языков: {page}: {links}")
            for target_language, actual in links.items():
                expected = "/" + target_language + "/" + route[target_language]
                if actual != expected:
                    raise ValueError(f"Неверная ссылка: {page}: {actual} вместо {expected}")
                if not (site / target_language / route[target_language] / "index.html").is_file():
                    raise FileNotFoundError(f"Целевая страница отсутствует: {expected}")


def rewrite_sitemaps(site: Path, mapping: dict[str, str]) -> tuple[int, int]:
    """Изменить адреса функций в sitemap.xml и сжатой sitemap.xml.gz."""
    files = replacements = 0
    for path in site.rglob("sitemap.xml"):
        original = path.read_text(encoding="utf-8")
        changed = original
        for old, new in mapping.items():
            # Важно: Lists/index.md имеет старый URL .../Lists/;
            # не заменяем его как префикс других функций в каталоге Lists.
            pattern = re.escape("ru/" + old) + r'(?=["<\s?#]|$)'
            changed, count = re.subn(pattern, lambda m: "ru/" + new, changed)
            replacements += count
        if changed != original:
            path.write_text(changed, encoding="utf-8")
            gz = path.with_suffix(path.suffix + ".gz")
            if gz.exists():
                gz.write_bytes(gzip.compress(changed.encode("utf-8"), mtime=0))
            files += 1
    return files, replacements

def validate(site: Path, mapping: dict[str, str]) -> None:
    # Проверяем, что все новые статьи и старые адреса существуют.
    for old, new in mapping.items():
        assert (site / "ru" / new / "index.html").is_file(), new
        assert (site / "ru" / old / "index.html").is_file(), old
    # В каждом поисковом индексе не должно остаться старых русских URL функций.
    for search_index in site.rglob("search_index.json"):
        data = json.loads(search_index.read_text(encoding="utf-8"))
        for item in data.get("docs", []):
            path = urlsplit("/" + item.get("location", "").lstrip("/")).path
            assert rewrite_site_path(path, mapping) == path, (search_index, path)


def localize(site: Path, config_file: Path) -> None:
    mapping = read_function_mapping(config_file)
    pages, links = rewrite_html_links(site, mapping)
    indices, search_entries = rewrite_search_indices(site, mapping)
    sitemap_files, sitemap_links = rewrite_sitemaps(site, mapping)
    moved = move_russian_pages(site, mapping)
    reverse_aliases = create_reverse_language_aliases(site, mapping)
    switcher_pages, switcher_links = fix_function_language_switcher(site, config_file)
    validate(site, mapping)
    validate_function_language_switcher(site, config_file)
    print(f"Russian function URLs: {moved} localized pages and old-URL redirects created.")
    print(f"EN/DE safety redirects: {reverse_aliases} Russian-slug aliases created.")
    print(f"Function language switcher EN/RU/DE: {switcher_links} links updated in {switcher_pages} pages.")
    print(f"Russian function URLs: {links} links updated in {pages} HTML pages.")
    print(f"Russian function URLs: {search_entries} search entries updated in {indices} indexes.")
    print(f"Russian function URLs: {sitemap_links} links updated in {sitemap_files} sitemaps.")


if __name__ == "__main__":
    localize(Path("docs"), Path("mkdocs.yml"))
