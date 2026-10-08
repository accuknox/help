/*
 * Adds the "New" badge to the AgentZ entry in the top tab bar and in the
 * primary sidebar. CSS alone cannot do it reliably, because Material rewrites
 * the href of the active tab, so an href selector drops the badge on the
 * AgentZ page itself. Matching on the label is stable in every state.
 */
(function () {
  var LABEL = "AgentZ";

  function decorate() {
    var links = document.querySelectorAll(
      ".md-tabs__link, .md-nav--primary > .md-nav__list > .md-nav__item > .md-nav__link"
    );
    links.forEach(function (link) {
      if (link.textContent.trim() !== LABEL) return;
      if (link.querySelector(".az-nav-badge")) return;
      var badge = document.createElement("span");
      badge.className = "az-nav-badge";
      badge.textContent = "New";
      link.appendChild(badge);
      link.classList.add("az-nav-link");
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(decorate);
  } else {
    document.addEventListener("DOMContentLoaded", decorate);
  }
})();
