// ============================================
// IAM Permissions tables — "why" tooltip
//
// The justification text lives in a `title` attribute on each `.iam-why`
// badge, so it works as a native tooltip even with zero JS. This script
// upgrades it to a styled, instant tooltip.
//
// Instant-navigation safe by design: listeners are delegated on `document`
// (attached once, never re-initialised per page) and the tooltip element is
// appended to `<body>` (so it escapes the table's overflow clipping). No
// per-page init, no inline data — the failure modes that broke the old
// interactive component simply don't apply here.
// ============================================
(function () {
  "use strict";
  var tip = null, current = null;

  function box() {
    if (!tip || !tip.isConnected) {
      tip = document.createElement("div");
      tip.className = "iam-tip";
      tip.setAttribute("role", "tooltip");
      document.body.appendChild(tip);
    }
    return tip;
  }

  function textFor(t) {
    // Move title -> data-why on first use so the native tooltip doesn't also fire.
    if (t.hasAttribute("title")) {
      t.setAttribute("data-why", t.getAttribute("title"));
      t.removeAttribute("title");
    }
    return t.getAttribute("data-why") || "";
  }

  function show(t) {
    var text = textFor(t);
    if (!text) return;
    var b = box();
    b.textContent = text;
    b.style.display = "block";
    b.style.maxWidth = Math.min(440, window.innerWidth - 24) + "px";
    var r = t.getBoundingClientRect();
    var left = r.left + window.scrollX;
    left = Math.min(left, window.scrollX + window.innerWidth - b.offsetWidth - 12);
    left = Math.max(window.scrollX + 8, left);
    var top = r.bottom + window.scrollY + 6;
    // flip above if there isn't room below
    if (r.bottom + b.offsetHeight + 14 > window.innerHeight) {
      top = r.top + window.scrollY - b.offsetHeight - 6;
    }
    b.style.left = left + "px";
    b.style.top = top + "px";
    current = t;
  }

  function hide() {
    if (tip) tip.style.display = "none";
    current = null;
  }

  document.addEventListener("mouseover", function (e) {
    var t = e.target.closest && e.target.closest(".iam-why");
    if (t) show(t);
  });
  document.addEventListener("mouseout", function (e) {
    var t = e.target.closest && e.target.closest(".iam-why");
    if (t) hide();
  });
  document.addEventListener("focusin", function (e) {
    var t = e.target.closest && e.target.closest(".iam-why");
    if (t) show(t);
  });
  document.addEventListener("focusout", function (e) {
    var t = e.target.closest && e.target.closest(".iam-why");
    if (t) hide();
  });
  // Tap-to-toggle for touch devices (no hover)
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest(".iam-why");
    if (!t) return;
    e.preventDefault();
    if (current === t) hide(); else show(t);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") hide();
  });
  window.addEventListener("scroll", function () { if (current) hide(); }, true);
  window.addEventListener("resize", hide);
})();
