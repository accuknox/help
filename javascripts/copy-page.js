// ============================================
// Copy page / View as Markdown / Open in ChatGPT / Open in Claude
// ============================================
// Injects a split-button at the top-right of every article. Options:
//   - Copy page         : copies the raw markdown to the clipboard
//   - View as Markdown  : opens the raw .md in a new tab
//   - Open in ChatGPT   : opens chatgpt.com with a prefilled prompt + URL
//   - Open in Claude    : opens claude.ai/new with a prefilled prompt + URL
//
// The raw markdown is published next to each page by the `copy_md_source.py`
// MkDocs hook, at `<page-url>index.md`.
//
// Works with Material's `navigation.instant` SPA navigation: re-runs on each
// `document$` emission so the button stays attached after client-side route
// changes.

(function () {
  function getMarkdownUrl() {
    let path = window.location.pathname;
    if (!path.endsWith("/")) path += "/";
    return path + "index.md";
  }

  async function fetchMarkdown() {
    const res = await fetch(getMarkdownUrl(), { cache: "no-store" });
    if (!res.ok) throw new Error("markdown fetch failed: " + res.status);
    return await res.text();
  }

  function buildPrompt() {
    const title = document.title || "this page";
    const url = window.location.href;
    return `Read ${url} and help me with questions about it. The page is titled "${title}".`;
  }

  function openChatGPT() {
    const q = encodeURIComponent(buildPrompt());
    window.open("https://chatgpt.com/?hints=search&q=" + q, "_blank", "noopener");
  }

  function openClaude() {
    const q = encodeURIComponent(buildPrompt());
    window.open("https://claude.ai/new?q=" + q, "_blank", "noopener");
  }

  async function copyPage(btn) {
    try {
      const md = await fetchMarkdown();
      await navigator.clipboard.writeText(md);
      flashLabel(btn, "Copied");
    } catch (e) {
      console.error(e);
      flashLabel(btn, "Failed");
    }
  }

  function viewAsMarkdown() {
    window.open(getMarkdownUrl(), "_blank", "noopener");
  }

  function flashLabel(btn, text) {
    const label = btn.querySelector(".ak-copy-page__label");
    if (!label) return;
    const prev = label.textContent;
    label.textContent = text;
    setTimeout(() => { label.textContent = prev; }, 1500);
  }

  function buildButton() {
    const wrap = document.createElement("div");
    wrap.className = "ak-copy-page";
    wrap.innerHTML = `
      <button type="button" class="ak-copy-page__main" aria-label="Copy page as markdown">
        <svg class="ak-copy-page__icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
        </svg>
        <span class="ak-copy-page__label">Copy page</span>
      </button>
      <button type="button" class="ak-copy-page__caret" aria-haspopup="menu" aria-expanded="false" aria-label="More copy options">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </button>
      <div class="ak-copy-page__menu" role="menu" hidden>
        <button type="button" role="menuitem" data-action="copy">
          <div class="ak-copy-page__menu-title">Copy page</div>
          <div class="ak-copy-page__menu-desc">Copy page as Markdown for LLMs</div>
        </button>
        <button type="button" role="menuitem" data-action="view">
          <div class="ak-copy-page__menu-title">View as Markdown <span class="ak-copy-page__ext">↗</span></div>
          <div class="ak-copy-page__menu-desc">View this page as plain text</div>
        </button>
        <button type="button" role="menuitem" data-action="chatgpt">
          <div class="ak-copy-page__menu-title">Open in ChatGPT <span class="ak-copy-page__ext">↗</span></div>
          <div class="ak-copy-page__menu-desc">Ask questions about this page</div>
        </button>
        <button type="button" role="menuitem" data-action="claude">
          <div class="ak-copy-page__menu-title">Open in Claude <span class="ak-copy-page__ext">↗</span></div>
          <div class="ak-copy-page__menu-desc">Ask questions about this page</div>
        </button>
      </div>
    `;

    const mainBtn = wrap.querySelector(".ak-copy-page__main");
    const caret = wrap.querySelector(".ak-copy-page__caret");
    const menu = wrap.querySelector(".ak-copy-page__menu");

    mainBtn.addEventListener("click", () => copyPage(mainBtn));

    caret.addEventListener("click", (e) => {
      e.stopPropagation();
      const open = !menu.hidden;
      menu.hidden = open;
      caret.setAttribute("aria-expanded", String(!open));
      if (!open) positionMenu(wrap, menu);
    });

    menu.addEventListener("click", (e) => {
      const item = e.target.closest("[data-action]");
      if (!item) return;
      const action = item.getAttribute("data-action");
      menu.hidden = true;
      caret.setAttribute("aria-expanded", "false");
      if (action === "copy") copyPage(mainBtn);
      else if (action === "view") viewAsMarkdown();
      else if (action === "chatgpt") openChatGPT();
      else if (action === "claude") openClaude();
    });

    document.addEventListener("click", (e) => {
      if (!wrap.contains(e.target)) {
        menu.hidden = true;
        caret.setAttribute("aria-expanded", "false");
      }
    });

    return wrap;
  }

  // The menu is wider than the TOC sidebar it hangs off, and Material's
  // `.md-sidebar__scrollwrap` is `overflow: auto` on both axes, so an
  // absolutely-positioned menu would be clipped there. In sidebar mode we
  // switch it to `position: fixed` and place it by hand, right-aligned to the
  // button and clamped into the viewport.
  function positionMenu(wrap, menu) {
    const inSidebar = wrap.classList.contains("ak-copy-page--sidebar");
    if (!inSidebar) {
      menu.style.position = "";
      menu.style.top = "";
      menu.style.left = "";
      return;
    }
    const b = wrap.getBoundingClientRect();
    menu.style.position = "fixed";
    menu.style.top = "auto";
    menu.style.left = "0px";
    // Measure after switching to fixed so the width is the real one.
    const m = menu.getBoundingClientRect();
    const pad = 8;
    let left = b.right - m.width;
    left = Math.min(left, window.innerWidth - m.width - pad);
    left = Math.max(pad, left);
    let top = b.bottom + 6;
    if (top + m.height > window.innerHeight - pad) {
      top = Math.max(pad, b.top - m.height - 6);
    }
    menu.style.left = left + "px";
    menu.style.top = top + "px";
  }

  // Where the button goes, in priority order:
  //   1. Top of the right-hand TOC sidebar, above "Table of contents". Fully
  //      outside the content flow, so it can never squeeze a heading.
  //   2. Its own right-aligned row above the H1, used when that sidebar is
  //      absent (`hide: toc`) or hidden by breakpoint (mobile/tablet).
  function tocTarget() {
    const sidebar = document.querySelector(".md-sidebar--secondary");
    if (!sidebar) return null;
    if (getComputedStyle(sidebar).display === "none") return null;
    return sidebar.querySelector(".md-sidebar__inner");
  }

  function place(wrap) {
    const target = tocTarget();
    if (target) {
      wrap.classList.add("ak-copy-page--sidebar");
      const host = document.createElement("div");
      host.className = "ak-copy-page-row ak-copy-page-row--sidebar";
      host.appendChild(wrap);
      target.prepend(host);
      return;
    }
    wrap.classList.remove("ak-copy-page--sidebar");
    const article = document.querySelector("article.md-content__inner");
    if (!article) return;
    const row = document.createElement("div");
    row.className = "ak-copy-page-row";
    row.appendChild(wrap);
    const h1 = article.querySelector("h1");
    if (h1) h1.parentNode.insertBefore(row, h1);
    else article.prepend(row);
  }

  function inject() {
    if (document.querySelector(".ak-copy-page")) return;
    const article = document.querySelector("article.md-content__inner");
    if (!article) return;
    // Landing pages opt out by dropping an `.ak-no-copy-page` marker in their
    // body. They are hand-built layouts with no prose to hand to an LLM, and
    // the button has nowhere sensible to sit.
    if (article.querySelector(".ak-no-copy-page")) return;
    place(buildButton());
  }

  // Crossing the sidebar breakpoint has to move the button, otherwise it would
  // sit inside a display:none sidebar and vanish on narrow viewports.
  function replaceOnResize() {
    const wrap = document.querySelector(".ak-copy-page");
    if (!wrap) return;
    const wantSidebar = !!tocTarget();
    const isSidebar = wrap.classList.contains("ak-copy-page--sidebar");
    if (wantSidebar === isSidebar) return;
    const oldRow = wrap.closest(".ak-copy-page-row");
    const menu = wrap.querySelector(".ak-copy-page__menu");
    menu.hidden = true;
    wrap.querySelector(".ak-copy-page__caret").setAttribute("aria-expanded", "false");
    place(wrap);
    if (oldRow && oldRow.parentNode) oldRow.remove();
  }

  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(replaceOnResize, 120);
  });

  if (window.document$) {
    window.document$.subscribe(() => inject());
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inject);
  } else {
    inject();
  }
})();
