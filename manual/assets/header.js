document.addEventListener("DOMContentLoaded", function () {

    const title = document.querySelector(".md-header__title");

    if (!title || document.querySelector(".home-icon-button")) {
        return;
    }



    title.prepend(link);
});