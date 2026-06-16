// ============================================
// 1. ANALYTICS/TRACKING
// ============================================
// Reo tracking
(function initializeReo() {
  const REO_CLIENT_ID = "ab7a909d0af3d55";
  const script = document.createElement("script");
  script.src = "https://static.reo.dev/" + REO_CLIENT_ID + "/reo.js";
  script.defer = true;
  script.onload = function () {
    Reo.init({ clientID: REO_CLIENT_ID });
  };
  document.head.appendChild(script);
})();

// Zoho Analytics/Insights tracking
(function initializeZohoAnalytics() {
  const ZOHO_PROJECT_KEY = "d1f7c795931728405066";
  const ZOHO_SCRIPT_URL = "https://js.zi-scripts.com/zi-tag.js";

  // Set the project key on window object (required by Zoho script)
  window.ZIProjectKey = ZOHO_PROJECT_KEY;

  // Create and configure the script element
  const script = document.createElement("script");
  script.type = "text/javascript";
  script.async = true;
  script.src = ZOHO_SCRIPT_URL;

  // Handle all document.readyState cases properly
  if (document.readyState === "loading") {
    // Document still loading - wait for DOMContentLoaded
    window.addEventListener("DOMContentLoaded", () => {
      document.body.appendChild(script);
    });
  } else {
    // Document is "interactive" or "complete" - safe to append immediately
    document.body.appendChild(script);
  }
})();

// ============================================
// 2. BETA LABELS FOR NAVIGATION
// ============================================
(function addBetaLabels() {
  const BETA_TOPICS = ["IoT/Edge Security", "5G Security"];

  // Find sidebar using stable Material for MkDocs class
  const sidebar = document.querySelector(".md-sidebar--primary");
  if (!sidebar) return;

  // Find all spans in navigation links within sidebar
  const navSpans = sidebar.querySelectorAll("nav a span");

  navSpans.forEach((span) => {
    const text = span.textContent.trim();
    const hasBetaTopic = BETA_TOPICS.some((topic) => text === topic);

    if (hasBetaTopic) {
      const parent = span.parentElement;
      if (parent && parent.tagName === "A") {
        parent.classList.add("new-label");
      }
    }
  });

  // Inject styles only once (check if already added)
  if (!document.getElementById("beta-label-styles")) {
    const style = document.createElement("style");
    style.id = "beta-label-styles";
    style.textContent = `
      .new-label::after {
        content: "Beta";
        background-color: #702963;
        color: white;
        font-size: 0.8em;
        border-radius: 4px;
        padding: 2px 6px;
        margin-left: 8px;
        text-transform: uppercase;
        display: inline-block;
      }
    `;
    document.head.appendChild(style);
  }
})();

// ============================================
// 3. GIST EMBEDS
// ============================================
// Loads GitHub Gists for <div class="gist-embed" data-gist-id="USER/ID"></div>.
// Uses JSONP to bypass CORS (fetch to gist.github.com is blocked cross-origin).
(function initGistEmbeds() {
  var loadedStylesheets = {};
  var callbackIndex = 0;

  function loadGist(el) {
    var gistId = el.getAttribute("data-gist-id");
    if (!gistId) return;

    var cbName = "__gistCb" + callbackIndex++;
    window[cbName] = function (data) {
      delete window[cbName];
      if (data.stylesheet && !loadedStylesheets[data.stylesheet]) {
        loadedStylesheets[data.stylesheet] = true;
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = data.stylesheet;
        document.head.appendChild(link);
      }
      el.innerHTML = data.div;
    };

    var s = document.createElement("script");
    s.src = "https://gist.github.com/" + gistId + ".json?callback=" + cbName;
    document.body.appendChild(s);
  }

  function loadGists() {
    document.querySelectorAll(".gist-embed:not([data-loaded])").forEach(function (el) {
      el.setAttribute("data-loaded", "true");
      loadGist(el);
    });
  }

  loadGists();

  if (typeof document$ !== "undefined") {
    document$.subscribe(loadGists);
  }
})();

// ============================================
// 4. TRAILING SLASH REDIRECT
// ============================================
// Ensures all help docs URLs have trailing slashes for proper image loading, ticket:CNAPP-24365
(function ensureTrailingSlash() {
  const ALLOWED_DOMAINS = ["help.accuknox.com", "test.help.accuknox.com"];

  // Only run on specified domains
  if (!ALLOWED_DOMAINS.includes(window.location.hostname)) {
    return;
  }

  const { pathname, search, hash } = window.location;

  // Skip if:
  // 1. Path is just "/" (root)
  // 2. Path already ends with "/"
  // 3. Path ends with a file extension (e.g., .html, .pdf, .png, .jpg, .svg, etc.)
  const isRoot = pathname === "/";
  const hasTrailingSlash = pathname.endsWith("/");
  const hasFileExtension = /\.([a-zA-Z0-9]+)$/.test(pathname);

  if (!isRoot && !hasTrailingSlash && !hasFileExtension) {
    // Redirect to the same URL with trailing slash
    // Using location.replace to avoid adding to browser history
    const newUrl = pathname + "/" + search + hash;
    window.location.replace(newUrl);
  }
})();
