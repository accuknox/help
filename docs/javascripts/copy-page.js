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

  function inject() {
    if (document.querySelector(".ak-copy-page")) return;
    const article = document.querySelector("article.md-content__inner");
    if (!article) return;
    const h1 = article.querySelector("h1");
    const btn = buildButton();
    if (h1) {
      h1.classList.add("ak-copy-page-h1");
      h1.parentNode.insertBefore(btn, h1);
    } else {
      article.prepend(btn);
    }
  }

  if (window.document$) {
    window.document$.subscribe(() => inject());
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inject);
  } else {
    inject();
  }
})();
