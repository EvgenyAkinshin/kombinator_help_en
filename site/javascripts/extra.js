// ================== ПОДСВЕТКА ЯКОРЕЙ (#...) В ТЕКСТЕ ==================

function applyHashHighlight() {
  // снять старую подсветку
  document
    .querySelectorAll(".hash-highlight")
    .forEach(el => el.classList.remove("hash-highlight"));

  const hash = window.location.hash;
  if (!hash) return;

  let target = null;
  try {
    target = document.querySelector(hash);
  } catch (e) {
    return;
  }
  if (!target) return;

  target.classList.add("hash-highlight");
}

// ================== РАСКРЫТИЕ ВСЕХ РАЗДЕЛОВ МЕНЮ ==================

function expandAllNavGroups() {
  // чекбоксы, которые отвечают за сворачивание/разворачивание
  const toggles = document.querySelectorAll('input.md-nav__toggle');

  toggles.forEach(toggle => {
    // если это именно чекбокс навигации — раскрываем
    if (toggle.type === "checkbox") {
      toggle.checked = true;
    }
  });
}

// ================== ОБЩИЙ ИНИЦИАЛИЗАТОР ==================

function initExtras() {
  applyHashHighlight();
  expandAllNavGroups();
}

// первый запуск после полной загрузки страницы
document.addEventListener("DOMContentLoaded", initExtras);

// если меняется только #... в адресе — обновляем подсветку, меню тут не трогаем
window.addEventListener("hashchange", applyHashHighlight);

// поддержка navigation.instant: после каждой подмены контента снова:
// 1) подсвечиваем якорь
// 2) раскрываем все разделы
if (typeof window.document$ !== "undefined") {
  window.document$.subscribe(() => {
    initExtras();
  });
}

/* =========================================================
   SEARCH: показываем результаты только после ввода текста
   ========================================================= */

function initSearchOutputVisibility() {
  const search = document.querySelector(".md-search");
  const input = document.querySelector(".md-search__input");

  if (!search || !input) {
    return;
  }

  function updateSearchState() {
    const hasValue = input.value.trim().length > 0;

    search.classList.toggle("search-has-value", hasValue);
  }

  input.addEventListener("input", updateSearchState);
  input.addEventListener("focus", updateSearchState);
  input.addEventListener("blur", updateSearchState);

  updateSearchState();
}

document.addEventListener("DOMContentLoaded", initSearchOutputVisibility);

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initSearchOutputVisibility();
  });
}

/* =========================================================
   SEARCH: меняем текст в строке поиска
   ========================================================= */

function initSearchPlaceholder() {
  const input = document.querySelector(".md-search__input");

  if (!input) {
    return;
  }

  input.setAttribute("placeholder", "Search articles, markers, or functions");
  input.setAttribute("aria-label", "Search articles, markers, or functions");
}

document.addEventListener("DOMContentLoaded", initSearchPlaceholder);

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initSearchPlaceholder();
  });
}

/* =========================================================
   RIGHT TOC: активный пункт строго по клику + корректный скролл
   ========================================================= */

function initRightTocActiveState() {
  const content = document.querySelector(".md-content__inner");
  const links = Array.from(
    document.querySelectorAll(".md-sidebar--secondary .md-nav__link[href*='#']")
  );

  if (!content || !links.length) {
    return;
  }

  /* Защита от повторной инициализации */
  if (content.dataset.rightTocReady === "true") {
    return;
  }

  content.dataset.rightTocReady = "true";

  const items = links
    .map(function (link) {
      const hash = new URL(link.href, window.location.href).hash;

      if (!hash) {
        return null;
      }

      const id = decodeURIComponent(hash.slice(1));
      const target = document.getElementById(id);

      if (!target) {
        return null;
      }

      return {
        link: link,
        target: target,
        hash: hash
      };
    })
    .filter(Boolean);

  if (!items.length) {
    return;
  }

  let clickedHash = null;
  let clickLockTimer = null;

  function setActive(activeLink) {
    links.forEach(function (link) {
      link.classList.remove("md-nav__link--active");
    });

    if (activeLink) {
      activeLink.classList.add("md-nav__link--active");
    }
  }

  function getScrollTopForTarget(target) {
    const contentRect = content.getBoundingClientRect();
    const targetRect = target.getBoundingClientRect();

    return content.scrollTop + targetRect.top - contentRect.top - 24;
  }

  function updateActiveByScroll() {
    /* Если пользователь только что кликнул по пункту,
       не даём автоскроллу перебить выбранный пункт */
    if (clickedHash) {
      return;
    }

    const contentTop = content.getBoundingClientRect().top;
    const activeOffset = 40;

    let current = items[0];

    items.forEach(function (item) {
      const offset = item.target.getBoundingClientRect().top - contentTop;

      if (offset <= activeOffset) {
        current = item;
      }
    });

    setActive(current.link);
  }

  let ticking = false;

  function onScroll() {
    if (ticking) {
      return;
    }

    window.requestAnimationFrame(function () {
      updateActiveByScroll();
      ticking = false;
    });

    ticking = true;
  }

  content.addEventListener("scroll", onScroll);
  window.addEventListener("scroll", onScroll);

  items.forEach(function (item) {
    item.link.addEventListener("click", function (event) {
      event.preventDefault();

      clickedHash = item.hash;

      if (clickLockTimer) {
        clearTimeout(clickLockTimer);
      }

      setActive(item.link);

      history.replaceState(null, "", item.hash);

      content.scrollTo({
        top: getScrollTopForTarget(item.target),
        behavior: "smooth"
      });

      /* Через 1 секунду снова разрешаем автоподсветку при ручной прокрутке.
         Но сразу после клика активный пункт не пересчитываем. */
      clickLockTimer = setTimeout(function () {
        clickedHash = null;
      }, 1000);
    });
  });

  updateActiveByScroll();
}

document.addEventListener("DOMContentLoaded", initRightTocActiveState);

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    setTimeout(initRightTocActiveState, 50);
  });
}

document.addEventListener("DOMContentLoaded", initRightTocActiveState);

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    setTimeout(initRightTocActiveState, 50);
  });
}