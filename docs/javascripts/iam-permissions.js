// ============================================
// IAM Permissions Reference — interactive renderer
//
// Renders any <div class="iam-perms" data-src="…json">. The permission data
// lives in an EXTERNAL JSON file loaded with fetch(), NOT in an inline
// <script> — Material's instant navigation re-processes inline <script> tags
// and strips the data block, which left the table blank until a hard refresh.
// Fetching sidesteps that entirely.
//
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

  function tagClass(t) {
    return TAG_CLASS[t] || "tag-default";
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  // ---- resolve + load the data, then render ----
  function buildOne(container) {
    if (container.dataset.iamReady === "1" || container.dataset.iamLoading === "1") return;

    var src = container.getAttribute("data-src");
    if (src) {
      container.dataset.iamLoading = "1";
      var loading = el("div", "iam-empty", "Loading permissions…");
      container.appendChild(loading);
      fetch(src)
        .then(function (r) {
          if (!r.ok) throw new Error("HTTP " + r.status);
          return r.json();
        })
        .then(function (payload) {
          container.dataset.iamLoading = "";
          if (loading.parentNode) loading.remove();
          render(container, payload);
        })
        .catch(function () {
          container.dataset.iamLoading = "";
          loading.textContent = "Could not load the permission list — please refresh the page.";
        });
      return;
    }

    // legacy fallback: inline <script type="application/json" class="iam-perms-data">
    var dataNode = container.querySelector("script.iam-perms-data");
    if (!dataNode) return;
    try {
      render(container, JSON.parse(dataNode.textContent));
    } catch (e) { /* no-op */ }
  }

  // ---- build the UI from a parsed payload ----
  function render(container, payload) {
    if (container.dataset.iamReady === "1") return;
    var records = (payload && payload.records) || [];

    // group by service, keep original order
    var groups = {};
    var order = [];
    records.forEach(function (r) {
      var s = r.s || "Other";
      if (!groups[s]) { groups[s] = []; order.push(s); }
      groups[s].push(r);
    });

    // toolbar
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
    order.forEach(function (service) {
      var det = el("details", "iam-group");
      det.dataset.service = service;
      var sum = el("summary", "iam-group-head");
      sum.innerHTML =
        '<span class="iam-group-name">' + escapeHtml(service) + "</span>" +
        '<span class="iam-group-count">' + groups[service].length + "</span>";
      det.appendChild(sum);
      var list = el("div", "iam-list");
      groups[service].forEach(function (r) { list.appendChild(buildRow(r)); });
      det.appendChild(list);
      groupsWrap.appendChild(det);
    });

    container.appendChild(toolbar);
    container.appendChild(empty);
    container.appendChild(groupsWrap);

    // interactions
    groupsWrap.addEventListener("click", function (e) {
      var perm = e.target.closest(".iam-perm");
      if (perm && !e.target.closest("a")) perm.classList.toggle("pinned");
    });
    document.addEventListener("click", function (e) {
      if (!container.contains(e.target)) {
        groupsWrap.querySelectorAll(".iam-perm.pinned").forEach(function (p) { p.classList.remove("pinned"); });
      }
    });
    container.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        groupsWrap.querySelectorAll(".iam-perm.pinned").forEach(function (p) { p.classList.remove("pinned"); });
      }
    });
    expandBtn.addEventListener("click", function () {
      groupsWrap.querySelectorAll("details.iam-group").forEach(function (d) {
        if (d.style.display !== "none") d.open = true;
      });
    });
    collapseBtn.addEventListener("click", function () {
      groupsWrap.querySelectorAll("details.iam-group").forEach(function (d) { d.open = false; });
    });

    var applyTimer;
    function apply() {
      var q = search.value.trim().toLowerCase();
      var svc = filter.value;
      var anyVisible = false;
      groupsWrap.querySelectorAll("details.iam-group").forEach(function (grp) {
        if (svc && grp.dataset.service !== svc) { grp.style.display = "none"; return; }
        var shown = 0;
        grp.querySelectorAll(".iam-perm").forEach(function (perm) {
          var match = !q || perm.dataset.search.indexOf(q) !== -1;
          perm.style.display = match ? "" : "none";
          if (match) shown++;
        });
        if (shown === 0) { grp.style.display = "none"; }
        else { grp.style.display = ""; anyVisible = true; if (q || svc) grp.open = true; }
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
    head.appendChild(el("code", "iam-perm-name", r.n));
    (r.t || []).forEach(function (t) {
      if (t) head.appendChild(el("span", "iam-tag " + tagClass(t), t));
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

    var hay = [r.n, r.s].concat(r.t || []);
    (r.d || []).forEach(function (p) { hay.push(p[1]); });
    row.dataset.search = hay.join(" ").toLowerCase();
    return row;
  }

  function init() {
    document.querySelectorAll("div.iam-perms").forEach(function (c) {
      try { buildOne(c); } catch (e) { /* keep subscription alive */ }
    });
  }

  // Hook Material's instant navigation (fires on initial load + every nav).
  // Retry until document$ exists so we never fall back to a one-time run that
  // misses instant navigation.
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
    if (document.readyState !== "loading") init();
    else document.addEventListener("DOMContentLoaded", init);
    var attempts = 0;
    var timer = setInterval(function () {
      attempts++;
      if (hookInstantNav() || attempts > 50) clearInterval(timer);
    }, 100);
  }
})();
