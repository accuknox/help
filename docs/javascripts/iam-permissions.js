// ============================================
// IAM Permissions Reference — interactive renderer
// Renders any <div class="iam-perms"> from its inline
// <script type="application/json" class="iam-perms-data"> payload.
// Compatible with Material instant navigation (document$).
// ============================================
(function () {
  "use strict";

  var TAG_CLASS = {
    "Asset inventory": "tag-inv",
    "Asset inventory and security checks": "tag-both",
    "Security checks": "tag-sec",
    "Scan coverage": "tag-scan",
    "get": "tag-inv",
    "list": "tag-inv",
    "getIamPolicy": "tag-sec"
  };

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function slug(s) {
    return String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }

  function tagClass(t) {
    return TAG_CLASS[t] || "tag-default";
  }

  function buildOne(container) {
    if (container.dataset.iamReady === "1") return;
    var dataNode = container.querySelector("script.iam-perms-data");
    if (!dataNode) return;

    var payload;
    try {
      payload = JSON.parse(dataNode.textContent);
    } catch (e) {
      return;
    }
    var records = payload.records || [];

    // ---- group by service, keep original order ----
    var groups = {};
    var order = [];
    records.forEach(function (r) {
      var s = r.s || "Other";
      if (!groups[s]) {
        groups[s] = [];
        order.push(s);
      }
      groups[s].push(r);
    });

    // ---- toolbar ----
    var toolbar = el("div", "iam-toolbar");

    var stats = el("div", "iam-stats");
    stats.innerHTML =
      '<span class="iam-count"><strong>' + records.length + "</strong> permissions</span>" +
      '<span class="iam-count"><strong>' + order.length + "</strong> services</span>" +
      '<span class="iam-badge-ro">Read-only</span>';
    toolbar.appendChild(stats);

    var controls = el("div", "iam-controls");

    var search = el("input", "iam-search");
    search.type = "search";
    search.placeholder = "Search permission, service or rationale…";
    search.setAttribute("aria-label", "Search permissions");
    controls.appendChild(search);

    var filter = el("select", "iam-service-filter");
    filter.setAttribute("aria-label", "Filter by service");
    filter.appendChild(new Option("All services", ""));
    order.slice().sort().forEach(function (s) {
      filter.appendChild(new Option(s + " (" + groups[s].length + ")", s));
    });
    controls.appendChild(filter);

    var expandBtn = el("button", "iam-btn", "Expand all");
    expandBtn.type = "button";
    var collapseBtn = el("button", "iam-btn", "Collapse all");
    collapseBtn.type = "button";
    controls.appendChild(expandBtn);
    controls.appendChild(collapseBtn);

    toolbar.appendChild(controls);

    var empty = el("div", "iam-empty", "No permissions match your search.");
    empty.style.display = "none";

    var groupsWrap = el("div", "iam-groups");

    // ---- render groups ----
    order.forEach(function (service) {
      var det = el("details", "iam-group");
      det.dataset.service = service;
      var sum = el("summary", "iam-group-head");
      sum.innerHTML =
        '<span class="iam-group-name">' + escapeHtml(service) + "</span>" +
        '<span class="iam-group-count">' + groups[service].length + "</span>";
      det.appendChild(sum);

      var list = el("div", "iam-list");
      groups[service].forEach(function (r) {
        list.appendChild(buildRow(r));
      });
      det.appendChild(list);
      groupsWrap.appendChild(det);
    });

    container.appendChild(toolbar);
    container.appendChild(empty);
    container.appendChild(groupsWrap);

    // ---- interactions ----
    groupsWrap.addEventListener("click", function (e) {
      var perm = e.target.closest(".iam-perm");
      if (perm && !e.target.closest("a")) {
        perm.classList.toggle("pinned");
      }
    });

    // close pinned popovers on outside click / Esc
    document.addEventListener("click", function (e) {
      if (!container.contains(e.target)) {
        groupsWrap.querySelectorAll(".iam-perm.pinned").forEach(function (p) {
          p.classList.remove("pinned");
        });
      }
    });
    container.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        groupsWrap.querySelectorAll(".iam-perm.pinned").forEach(function (p) {
          p.classList.remove("pinned");
        });
      }
    });

    expandBtn.addEventListener("click", function () {
      groupsWrap.querySelectorAll("details.iam-group").forEach(function (d) {
        if (d.style.display !== "none") d.open = true;
      });
    });
    collapseBtn.addEventListener("click", function () {
      groupsWrap.querySelectorAll("details.iam-group").forEach(function (d) {
        d.open = false;
      });
    });

    var applyTimer;
    function apply() {
      var q = search.value.trim().toLowerCase();
      var svc = filter.value;
      var anyVisible = false;

      groupsWrap.querySelectorAll("details.iam-group").forEach(function (grp) {
        if (svc && grp.dataset.service !== svc) {
          grp.style.display = "none";
          return;
        }
        var shown = 0;
        grp.querySelectorAll(".iam-perm").forEach(function (perm) {
          var hay = perm.dataset.search;
          var match = !q || hay.indexOf(q) !== -1;
          perm.style.display = match ? "" : "none";
          if (match) shown++;
        });
        if (shown === 0) {
          grp.style.display = "none";
        } else {
          grp.style.display = "";
          anyVisible = true;
          // auto-open when actively searching/filtering
          if (q || svc) grp.open = true;
        }
      });
      empty.style.display = anyVisible ? "none" : "";
    }

    search.addEventListener("input", function () {
      clearTimeout(applyTimer);
      applyTimer = setTimeout(apply, 120);
    });
    filter.addEventListener("change", apply);

    container.dataset.iamReady = "1";
  }

  function buildRow(r) {
    var row = el("div", "iam-perm");
    row.tabIndex = 0;

    var head = el("div", "iam-perm-head");
    var name = el("code", "iam-perm-name", r.n);
    head.appendChild(name);

    (r.t || []).forEach(function (t) {
      if (!t) return;
      head.appendChild(el("span", "iam-tag " + tagClass(t), t));
    });
    row.appendChild(head);

    var pop = el("div", "iam-pop");
    var popName = el("div", "iam-pop-name");
    popName.appendChild(el("code", null, r.n));
    if (r.s) popName.appendChild(el("span", "iam-pop-svc", r.s));
    pop.appendChild(popName);

    (r.d || []).forEach(function (pair) {
      if (!pair[1]) return;
      var block = el("div", "iam-pop-row");
      block.appendChild(el("span", "iam-pop-label", pair[0]));
      block.appendChild(el("span", "iam-pop-text", pair[1]));
      pop.appendChild(block);
    });
    row.appendChild(pop);

    // searchable haystack
    var hay = [r.n, r.s].concat(r.t || []);
    (r.d || []).forEach(function (p) { hay.push(p[1]); });
    row.dataset.search = hay.join(" ").toLowerCase();

    return row;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function init() {
    document.querySelectorAll("div.iam-perms").forEach(function (c) {
      // guard each build so one bad page can never kill the subscription
      try { buildOne(c); } catch (e) { /* no-op */ }
    });
  }

  // Primary path: Material's instant navigation emits `document$` on the initial
  // load AND on every in-app navigation. Subscribing once handles all of them.
  // The catch is that `document$` may not exist yet at the moment this script
  // runs (script/bundle order), which would otherwise leave us on a one-time
  // DOMContentLoaded fallback that never fires on instant navigation. So we hook
  // it as soon as it appears, and still render the current page in the meantime.
  var subscribed = false;
  function hookInstantNav() {
    if (subscribed) return true;
    if (window.document$ && typeof window.document$.subscribe === "function") {
      subscribed = true;
      window.document$.subscribe(init);
      return true;
    }
    return false;
  }

  if (!hookInstantNav()) {
    // render whatever is on screen right now...
    if (document.readyState !== "loading") init();
    else document.addEventListener("DOMContentLoaded", init);
    // ...and keep trying to attach to instant navigation until Material is ready
    var attempts = 0;
    var timer = setInterval(function () {
      attempts++;
      if (hookInstantNav() || attempts > 50) clearInterval(timer);
    }, 100);
  }
})();
