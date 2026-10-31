from pathlib import Path
import shutil
import subprocess
import sys

# Сборка сайта стандартным способом
subprocess.run(
    [sys.executable, "-m", "mkdocs", "build"],
    check=True
)

site = Path("docs")
english = site / "en"

# Копирование английской версии в /en/
english.mkdir(exist_ok=True)

for item in list(site.iterdir()):
    if item.name in ("en", "ru", "de"):
        continue

    target = english / item.name

    if item.is_dir():
        shutil.copytree(item, target, dirs_exist_ok=True)
    elif item.name != "CNAME":
        shutil.copy2(item, target)

print("English pages copied to /en/")


from html import escape

# Перенаправление для отсутствующих немецких статей
german = site / "de"

for english_page in english.rglob("index.html"):
    relative_path = english_page.relative_to(english)

    german_page = german / relative_path

    # Настоящий немецкий перевод не заменяем
    if german_page.exists():
        continue

    target_url = "/en/" + relative_path.parent.as_posix().strip("/")
    if not target_url.endswith("/"):
        target_url += "/"

    german_page.parent.mkdir(parents=True, exist_ok=True)

    safe_url = escape(target_url, quote=True)

    german_page.write_text(
        f'<!doctype html><html lang="de"><head>'
        f'<meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0;url={safe_url}">'
        f'<link rel="canonical" href="{safe_url}">'
        f'</head><body>'
        f'<a href="{safe_url}">Open English version</a>'
        f'</body></html>',
        encoding="utf-8"
    )

print("German fallback redirects created.")


# Перенаправление с главной страницы на английскую версию

root_index = site / "index.html"

root_index.write_text(
    """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0;url=/en/">
  <link rel="canonical" href="/en/">
  <title>Kombinator Help</title>
</head>
<body>
  <p>Redirecting to <a href="/en/">English documentation</a>.</p>
</body>
</html>""",
    encoding="utf-8"
)

print("Homepage redirect to /en/ created.")

# Перенаправление старых английских адресов на /en/

from html import escape

for english_page in english.rglob("index.html"):
    relative_path = english_page.relative_to(english)

    # Главная страница уже перенаправляется на /en/
    if relative_path == Path("index.html"):
        continue

    old_page = site / relative_path

    # Не затрагиваем страницы других языков
    if relative_path.parts[0] in ("en", "ru", "de"):
        continue

    target_url = "/en/" + relative_path.parent.as_posix().strip("/") + "/"
    safe_url = escape(target_url, quote=True)

    old_page.parent.mkdir(parents=True, exist_ok=True)

    old_page.write_text(
        f'<!doctype html><html lang="en"><head>'
        f'<meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0;url={safe_url}">'
        f'<link rel="canonical" href="{safe_url}">'
        f'</head><body>'
        f'<a href="{safe_url}">Open English version</a>'
        f'</body></html>',
        encoding="utf-8"
    )

print("Old English URLs redirect to /en/")
