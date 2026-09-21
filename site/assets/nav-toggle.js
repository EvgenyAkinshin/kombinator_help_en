const SCROLL_KEY = "mkdocs-left-menu-scroll";

function getScrollwrap() {
  return document.querySelector(".md-sidebar--primary .md-sidebar__scrollwrap");
}

function restoreScroll() {
  const scrollwrap = getScrollwrap();
  const saved = sessionStorage.getItem(SCROLL_KEY);

  if (!scrollwrap || saved === null) return;

  const value = Number(saved);

  setTimeout(() => scrollwrap.scrollTop = value, 50);
  setTimeout(() => scrollwrap.scrollTop = value, 150);
  setTimeout(() => scrollwrap.scrollTop = value, 300);
}

function initThirdLevelMenu() {
  const sidebar = document.querySelector(".md-sidebar--primary");
  const scrollwrap = getScrollwrap();

  if (!sidebar) return;

  sidebar.querySelectorAll(".md-nav__item--nested").forEach(function (item) {
    const thirdLevel = item.querySelector(":scope > .md-nav[data-md-level='2']");
    if (!thirdLevel) return;

    const link = item.querySelector(":scope > .md-nav__link");

    if (!link || link.dataset.thirdToggleReady === "true") return;

    link.dataset.thirdToggleReady = "true";

    link.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();

      item.classList.toggle("third-level-open");
    });
  });

  if (scrollwrap) {
    restoreScroll();

    scrollwrap.addEventListener("scroll", function () {
      sessionStorage.setItem(SCROLL_KEY, String(scrollwrap.scrollTop));
    });
  }
}

document.addEventListener("DOMContentLoaded", initThirdLevelMenu);

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initThirdLevelMenu();
    restoreScroll();
  });
}