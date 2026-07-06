---
title: AccuKnox Help Center
description: AccuKnox Help Center is a one-stop destination for all your queries related to AccuKnox products. Get started with our product documentation, FAQs, and more.
hide:
  - navigation
  - toc
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

  /* Reset & Base */
  h1 {
      display: none !important;
  }

  /* Fonts */
  body, .md-typeset, .md-typeset h1, .md-typeset h2, .md-typeset h3, .md-typeset h4, .md-typeset h5, .md-typeset h6 {
      font-family: 'Poppins', sans-serif !important;
  }

  /* Ensure the main content stretches fully without creating a horizontal gap */
  .md-main__inner {
    width: 100% !important;
    max-width: 100% !important;
    padding: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    margin-bottom: 0 !important;
    overflow-x: hidden; /* prevents tiny horizontal gaps near the scrollbar */
    overflow-y: visible;
    box-sizing: border-box;
    margin-top: -10px !important; /* Adjust negative margin to close the gap */
  }

  .md-content {
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
  }

  /* Make page sections full-bleed edge-to-edge across the viewport */
  .md-typeset section,
  .md-typeset .hero-section,
  .md-typeset .explorer-section,
  .md-typeset .use-cases-section,
  .integrations-container,
  .section5-container,
  .home-section-7 {
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    width: 100vw;
    padding-left: 60px; /* keep inner spacing */
    padding-right: 60px;
    box-sizing: border-box;
  }

  /* Allow internal containers to expand to full width where needed */
  .modules-container, .use-cases-grid, .modules-content, .integrations-container .text-container-int {
    max-width: none !important;
    width: 100% !important;
    margin: 0 auto;
  }

  /* Prevent horizontal scroll on small screens */
  html, body, .md-main__inner { overflow-x: hidden; }

  /* Make hero section full-bleed so its background reaches the viewport edge */
  .hero-section {
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    width: 100vw;
    padding-left: 20px; /* keep the original inner spacing */
    padding-right: 20px;
  }

  /* SECTION 1: HERO */
  .hero-section {
    background-color: #000028; /* Dark blue match */
    color: white;
    text-align: center;
    padding: 60px 20px;
    font-family: 'Poppins', sans-serif;
  }

  .hero-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: white;
  }

  .hero-subtitle {
    font-size: 1rem;
    color: #cbd5e1;
    margin-bottom: 3rem;
    font-weight: 300;
  }

  /* CAROUSEL STYLES */
  .carousel-container {
    perspective: 1000px;
    width: 100%;
    margin-top: 40px;
    display: flex;
    justify-content: center;
    position: relative;
    height: 400px;
  }

  .carousel-card {
    background-color: #e6ecf2;
    border-radius: 8px;
    position: absolute;
    width: 60%;
    max-width: 700px;
    height: 100%;
    transition: all 0.6s cubic-bezier(0.25, 0.8, 0.25, 1);
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    overflow: hidden;
    /* Default Hidden State */
    opacity: 0;
    z-index: 0;
    transform: translateX(0) scale(0.5);
    background-color: #cbd5e1;
  }

  /* Center Card: Front and flat */
  .card-center {
    z-index: 3;
    transform: translateX(0) scale(1);
    opacity: 1;
    background-color: #e6ecf2;
  }

  /* Left Card: Pushed back, rotated Y, moved left */
  .card-left {
    z-index: 2; /* Higher than hidden, lower than center */
    transform: translateX(-55%) scale(0.8) rotateY(25deg);
    opacity: 0.6;
    background-color: #cbd5e1; /* Darker to simulate shadow */
  }

  /* Right Card: Pushed back, rotated Y, moved right */
  .card-right {
    z-index: 2;
    transform: translateX(55%) scale(0.8) rotateY(-25deg);
    opacity: 0.6;
    background-color: #cbd5e1;
  }

  /* Hover effects for side cards to invite interaction */
  .card-left:hover, .card-right:hover {
      opacity: 0.8;
  }

  /* SECTION 2: EXPLORER */
  .explorer-section {
    padding: 40px 20px;
    background-color: #ffffff;
    font-family: 'Poppins', sans-serif;
  }

  .explorer-title {
    text-align: center;
    font-size: 1.75rem;
    font-weight: 700;
    color: #000;
    margin-bottom: 30px;
  }

  /* Tabs */
  .tabs-container {
    display: flex;
    justify-content: center;
    gap: 6px;
    margin-bottom: 30px;
    flex-wrap: nowrap; /* keep tabs on one line */
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    background: #f8fafc;
    padding: 6px;
    border-radius: 32px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
    white-space: nowrap;
  }

  .tab-btn {
    background: transparent;
    border: none;
    padding: 6px 10px; /* reduced padding */
    border-radius: 12px; /* smaller radius */
    cursor: pointer;
    font-size: 0.82rem; /* slightly smaller text */
    font-weight: 600;
    color: #64748b;
    display: inline-flex;
    align-items: center;
    gap: 4px; /* reduced gap between icon and text */
    transition: all 0.18s;
    white-space: nowrap;
    min-width: 0; /* allow tight shrink */
  }

  /* Ensure tab icons transition smoothly and are visible when active */
  .tab-btn img {
    transition: filter 0.2s ease, opacity 0.2s ease;
    width: 14px;
    height: 14px;
    opacity: 0.95;
  }

  .tab-btn.active {
    background-color: #0f172a; /* Dark active state */
    color: white;
  }

  /* Make icons white when tab is active for visibility on dark background */
  .tab-btn.active img {
    filter: brightness(0) invert(1);
    opacity: 1;
  }

  .tab-btn:hover:not(.active) {
    background-color: #e2e8f0;
  }

  /* Modules Split View */
  .modules-container {
    display: flex;
    max-width: 1200px;
    margin: 0 auto;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    min-height: 500px;
  }

  .modules-sidebar {
    width: 25%;
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
    padding: 20px 0;
  }

  .module-item {
    padding: 15px 20px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    color: #475569;
    font-weight: 500;
    transition: background 0.2s;
    border-left: 3px solid transparent;
  }

  .module-item:hover {
    background-color: #f1f5f9;
  }

  .module-item.active {
    background-color: #eff6ff;
    color: #2563eb;
    border-left-color: #2563eb;
  }

  .module-icon {
      width: 18px;
      height: 18px;
      opacity: 0.7;
  }

  .modules-content {
    width: 75%;
    background-color: #f8fafc;
    padding: 40px;
    display: flex;
    flex-direction: column;
  }

  .content-header {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }

  .action-btn {
    background-color: #2563eb !important;
    border: 1px solid #2563eb !important;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 0.85rem;
    color: white !important;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-weight: 500;
    transition: all 0.2s ease;
  }
  /* Ensure all buttons look the same, overriding any previous first-child logic */
  .action-btn:first-child {
      background-color: #2563eb !important;
      color: white !important;
      border-color: #2563eb !important;
  }
  .action-btn::after {
      content: "→";
      transition: transform 0.2s;
  }
  .action-btn:hover {
      background-color: #1d4ed8 !important;
      border-color: #1d4ed8 !important;
      color: white !important;
  }
  .action-btn:hover::after {
      transform: translateX(3px);
  }

  .module-detail-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
  }

  .agentless-badge {
    background-color: #dbeafe;
    color: #1e40af;
    font-size: 0.75rem;
    padding: 2px 8px;
    border-radius: 4px;
    vertical-align: middle;
  }

  .module-description {
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 30px;
    max-width: 800px;
  }

  .module-visual-placeholder {
    flex-grow: 1;
    background-color: #e2e8f0; /* darker placeholder */
    border-radius: 8px;
    margin-bottom: 20px;
    min-height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #94a3b8;
  }

  .learn-more-link {
    color: #2563eb;
    text-decoration: none;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
  }
  .learn-more-link:hover {
      text-decoration: underline;
  }

  /* SECTION 3: USE CASES (Resyled) */
  .use-cases-section {
    padding: 60px 40px;
    background-color: #ffffff;
    font-family: 'Poppins', sans-serif;
  }

  .section-heading-3 {
      text-align: center;
      font-size: 1.8rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 40px;
  }

  .use-cases-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .use-case-card {
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
      background: white;
      transition: all 0.2s ease;
  }

  .use-case-card:hover {
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      border-color: #cbd5e1;
  }

  .use-case-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      padding-bottom: 15px;
      border-bottom: 1px solid #f1f5f9;
  }

  .use-case-icon {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
  }

  /* Icon variants based on image colors approximately */
  .icon-blue { background-color: #eff6ff; color: #3b82f6; } /* Light blue bg, Blue icon */
  .icon-indigo { background-color: #eef2ff; color: #6366f1; }
  .icon-sky { background-color: #f0f9ff; color: #0ea5e9; }


  .use-case-title {
      font-size: 1.1rem !important; /* Override MD styles */
      font-weight: 700 !important;
      color: #0f172a !important;
      margin: 0 !important;
      padding: 0 !important;
      border: none !important;
      display: block !important;
      line-height: 1.3;
  }

  .use-case-list {
      list-style: none;
      padding: 0;
      margin: 0;
  }

  .use-case-list li {
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
  }

  .use-case-list li::before {
      content: "›"; /* Simple arrow, or use background image */
      color: #3b82f6;
      font-weight: bold;
      font-size: 1.2rem;
      line-height: 1rem;
  }

  .use-case-list a {
      color: #64748b;
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
      line-height: 1.4;
  }

  .use-case-list a:hover {
      color: #2563eb;
  }

  .view-all-btn {
      display: block;
      width: fit-content;
      margin: 40px auto 0;
      padding: 12px 24px;
      background-color: #2563eb;
      color: white !important;
      text-decoration: none;
      border-radius: 6px;
      font-weight: 600;
  }
  .view-all-btn:hover {
      background-color: #1e40af;
  }

  /* EXISTING SECTIONS STYLES RETAINED PARTIALLY FOR COMPATIBILITY */
  /* Section 4, 5, 7 styles */
  .integrations-container {
    display: flex;
    align-items: center;
    background-color: #000025;
    padding: 80px 40px;
    font-family: 'Poppins', sans-serif;
  }
  .image-container2 { flex: 1; display: flex; justify-content: center; }
  .integrations-image { max-width: 100%; height: auto; }
  .text-container-int { flex: 1; color: #fff; margin-left: 40px; }
.integrations-title { font-weight: 900; font-size: 2rem; margin-bottom: 1rem; line-height: 1.2; color: white;}
  .integrations-description { font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; color: #cbd5e1; }
  .btn-style { background-color: #2563eb; color: white !important; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block; font-weight: bold; border:none; cursor: pointer;}

  .section5-container { background-color: #f9f9fc; padding: 60px 20px; text-align: center; font-family: 'Poppins', sans-serif;}
  .section5-card-container { display: flex; justify-content: center; gap: 30px; margin-top: 40px; flex-wrap: wrap;}
  .section5-card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); width: 350px; text-align: center; }
  .section5-card img { width: 60px; margin-bottom: 15px; }
  .section5-card-title { font-size: 1.1rem; font-weight: bold; margin-bottom: 10px; color: #0f172a;}
  .section5-card-link { color: #2563eb; font-weight: 600; text-decoration: none; }

  .home-section-7 { padding: 40px 0; text-align: center; background: white; font-family: 'Poppins', sans-serif;}
  .section7-nav { display: flex; justify-content: center; gap: 40px; margin-top: 20px; }
  .section7-link { color: #2563eb; font-weight: 700; text-decoration: none; padding-right: 20px; border-right: 1px solid #cbd5e1; }
  .section7-link:last-child { border-right: none; }

  .section-heading {
      text-align: center;
      color: #030372;
      font-size: 1.8rem !important;
      font-weight: 900 !important;
      text-align: center;
      margin-bottom: 10px;
  }

  @media (max-width: 991px) {
    .modules-container { flex-direction: column; }
    .modules-sidebar { width: 100%; border-right: none; border-bottom: 1px solid #e2e8f0; display: flex; overflow-x: auto;}
    .modules-content { width: 100%; }
    .integrations-container { flex-direction: column; text-align: center; }
    .text-container-int { margin-left: 0; margin-top: 30px; }
    .use-cases-grid { grid-template-columns: 1fr; }
  }

  /* =====================================================
     HOMEPAGE DARK MODE OVERRIDES
     Targets every hardcoded section for slate scheme
     ===================================================== */
  [data-md-color-scheme="slate"] .hero-section {
    background-color: #060a14;
  }

  /* SECTION 2: Explorer / Modules */
  [data-md-color-scheme="slate"] .explorer-section {
    background-color: #0b0f19;
  }

  [data-md-color-scheme="slate"] .explorer-title {
    color: #f1f5f9 !important;
  }

  [data-md-color-scheme="slate"] .tabs-container {
    background: #111827;
    border: 1px solid rgba(148, 163, 184, 0.1);
  }

  [data-md-color-scheme="slate"] .tab-btn {
    color: #94a3b8;
  }

  [data-md-color-scheme="slate"] .tab-btn.active {
    background-color: #3b82f6;
    color: #ffffff;
  }

  [data-md-color-scheme="slate"] .tab-btn:hover:not(.active) {
    background-color: #1e293b;
    color: #e2e8f0;
  }

  /* Invert tab icons in dark mode for visibility */
  [data-md-color-scheme="slate"] .tab-btn img {
    filter: brightness(0) invert(0.7);
  }
  [data-md-color-scheme="slate"] .tab-btn.active img {
    filter: brightness(0) invert(1);
  }

  [data-md-color-scheme="slate"] .modules-container {
    border-color: rgba(148, 163, 184, 0.1);
    background-color: #111827;
  }

  [data-md-color-scheme="slate"] .modules-sidebar {
    background-color: #0d1220;
    border-right-color: rgba(148, 163, 184, 0.08);
  }

  [data-md-color-scheme="slate"] .module-item {
    color: #94a3b8;
    border-left-color: transparent;
  }

  [data-md-color-scheme="slate"] .module-item:hover {
    background-color: #1e293b;
    color: #e2e8f0;
  }

  [data-md-color-scheme="slate"] .module-item.active {
    background-color: rgba(59, 130, 246, 0.1);
    color: #60a5fa;
    border-left-color: #3b82f6;
  }

  [data-md-color-scheme="slate"] .module-item img {
    filter: brightness(0) invert(0.6);
  }
  [data-md-color-scheme="slate"] .module-item.active img {
    filter: brightness(0) invert(0.7) sepia(1) saturate(5) hue-rotate(190deg);
  }

  [data-md-color-scheme="slate"] .modules-content {
    background-color: #111827;
  }

  [data-md-color-scheme="slate"] .module-detail-title {
    color: #f1f5f9;
  }

  [data-md-color-scheme="slate"] .module-description {
    color: #94a3b8;
  }

  [data-md-color-scheme="slate"] .agentless-badge {
    background-color: rgba(59, 130, 246, 0.15);
    color: #60a5fa;
  }

  [data-md-color-scheme="slate"] .module-visual-placeholder {
    background-color: #1e293b;
    border: 1px solid rgba(148, 163, 184, 0.08);
  }

  [data-md-color-scheme="slate"] .learn-more-link {
    color: #60a5fa;
  }

  [data-md-color-scheme="slate"] .action-btn {
    background-color: #2563eb !important;
    border-color: #2563eb !important;
    color: #ffffff !important;
  }
  [data-md-color-scheme="slate"] .action-btn:hover {
    background-color: #3b82f6 !important;
    border-color: #3b82f6 !important;
  }

  /* SECTION 3: Use Cases / Popular Resources */
  [data-md-color-scheme="slate"] .use-cases-section {
    background-color: #0b0f19;
  }

  [data-md-color-scheme="slate"] .section-heading-3 {
    color: #f1f5f9 !important;
  }

  [data-md-color-scheme="slate"] .use-case-card {
    background-color: #111827;
    border-color: rgba(148, 163, 184, 0.1);
  }

  [data-md-color-scheme="slate"] .use-case-card:hover {
    border-color: rgba(59, 130, 246, 0.3);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.08);
  }

  [data-md-color-scheme="slate"] .use-case-header {
    border-bottom-color: rgba(148, 163, 184, 0.08);
  }

  [data-md-color-scheme="slate"] .use-case-title {
    color: #e2e8f0 !important;
  }

  [data-md-color-scheme="slate"] .use-case-icon.icon-blue {
    background-color: rgba(59, 130, 246, 0.12);
  }
  [data-md-color-scheme="slate"] .use-case-icon.icon-indigo {
    background-color: rgba(99, 102, 241, 0.12);
  }
  [data-md-color-scheme="slate"] .use-case-icon.icon-sky {
    background-color: rgba(14, 165, 233, 0.12);
  }

  [data-md-color-scheme="slate"] .use-case-list a {
    color: #94a3b8;
  }

  [data-md-color-scheme="slate"] .use-case-list a:hover {
    color: #60a5fa;
  }

  [data-md-color-scheme="slate"] .view-all-btn {
    background-color: #3b82f6;
  }
  [data-md-color-scheme="slate"] .view-all-btn:hover {
    background-color: #2563eb;
  }

  /* SECTION 4: Integrations (already dark, but refine) */
  [data-md-color-scheme="slate"] .integrations-container {
    background-color: #060a14;
    border-top: 1px solid rgba(148, 163, 184, 0.06);
    border-bottom: 1px solid rgba(148, 163, 184, 0.06);
  }

  /* SECTION 5: Technical Support */
  [data-md-color-scheme="slate"] .section5-container {
    background-color: #0b0f19;
  }

  [data-md-color-scheme="slate"] .section-heading {
    color: #e2e8f0 !important;
  }

  [data-md-color-scheme="slate"] .section5-card {
    background-color: #111827;
    border: 1px solid rgba(148, 163, 184, 0.1);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }

  [data-md-color-scheme="slate"] .section5-card-title {
    color: #e2e8f0;
  }

  [data-md-color-scheme="slate"] .section5-card p {
    color: #94a3b8;
  }

  [data-md-color-scheme="slate"] .section5-card-link {
    color: #60a5fa;
  }

  /* SECTION 7: Find Out More */
  [data-md-color-scheme="slate"] .home-section-7 {
    background-color: #0b0f19 !important;
  }

  [data-md-color-scheme="slate"] .section7-link {
    color: #60a5fa;
    border-right-color: #334155;
  }

  /* Carousel dark mode */
  [data-md-color-scheme="slate"] .carousel-card {
    background-color: #1e293b;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  }
  [data-md-color-scheme="slate"] .card-center {
    background-color: #1e293b;
  }
  [data-md-color-scheme="slate"] .card-left,
  [data-md-color-scheme="slate"] .card-right {
    background-color: #111827;
  }

  /* Responsive dark overrides */
  @media (max-width: 991px) {
    [data-md-color-scheme="slate"] .modules-sidebar {
      border-bottom-color: rgba(148, 163, 184, 0.08);
    }
  }
</style>

<section class="hero-section">
  <div class="hero-title">Welcome to AccuKnox Help Center</div>
  <div class="hero-subtitle">Explore our comprehensive documentation and resources for cloud-native security</div>

  <div class="carousel-container" id="heroCarousel">
      <div class="carousel-card card-left" onclick="rotateCarousel('left')">
         <img src="assets/images/homepage/1.png" alt="Carousel Image 1" style="border-radius: 8px;">
      </div>

      <div class="carousel-card card-center" onclick="/* Center click */">
          <img src="assets/images/homepage/2.png" alt="Carousel Image 2" style=" border-radius: 8px;">
      </div>

      <div class="carousel-card card-right" onclick="rotateCarousel('right')">
          <img src="assets/images/homepage/3.png" alt="Carousel Image 3" style=" border-radius: 8px;">
      </div>

      <div class="carousel-card" onclick="/* hidden */">
        <img src="assets/images/homepage/4.png" alt="Carousel Image 4" style=" border-radius: 8px;">
      </div>

      <div class="carousel-card" onclick="/* hidden */">
        <img src="assets/images/homepage/5.png" alt="Carousel Image 5" style=" border-radius: 8px;">
      </div>

  </div>
</section>

<section class="explorer-section">
  <div class="explorer-title" style="font-size: 1.8rem; font-weight: 800; text-align: center; color: #0f172a; margin-bottom: 25px;">AccuKnox - Security for the AI Era</div>

  <div class="tabs-container" id="categoryTabs">
    <button class="tab-btn active" onclick="selectCategory('code', this)">
        <img src="assets/icons/code.svg" alt="Secure Code" width="14" height="14" style="vertical-align:text-bottom; margin-right:6px;" /> Secure Code & APIs
    </button>
    <button class="tab-btn" onclick="selectCategory('cloud', this)">
        <img src="assets/icons/cloud.svg" alt="Secure Cloud" width="14" height="14" style="vertical-align:text-bottom; margin-right:6px;" /> Secure Cloud
    </button>
    <button class="tab-btn" onclick="selectCategory('workloads', this)">
        <img src="assets/icons/workloads.svg" alt="Secure Workloads" width="14" height="14" style="vertical-align:text-bottom; margin-right:6px;" /> Secure Workloads
    </button>
    <button class="tab-btn" onclick="selectCategory('ai', this)">
        <img src="assets/icons/ai.svg" alt="Secure AI" width="14" height="14" style="vertical-align:text-bottom; margin-right:6px;" /> Secure AI
    </button>
    <button class="tab-btn" onclick="selectCategory('onprem', this)">
        <img src="assets/icons/onprem.svg" alt="On-Prem" width="14" height="14" style="vertical-align:text-bottom; margin-right:6px;" /> Secure On-Premise
    </button>
    <button class="tab-btn" onclick="selectCategory('compliance', this)">
        <img src="assets/icons/compliance.svg" alt="Compliance" width="14" height="14" style="vertical-align:text-bottom; margin-right:6px;" /> Compliance
    </button>
  </div>

  <div class="modules-container">
    <div class="modules-sidebar" id="modulesList">
      <div class="module-item active" data-cat="code" onclick="selectModule('devsecops', this)">
         <img src="assets/icons/shield.svg" alt="DevSecOps" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> DevSecOps (ASPM)
      </div>
      <div class="module-item" data-cat="code" onclick="selectModule('api', this)">
         <img src="assets/icons/api.svg" alt="API Security" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> API Security
      </div>
      <div class="module-item" data-cat="cloud" style="display:none;" onclick="selectModule('cspm', this)">
         <img src="assets/icons/cloud.svg" alt="Cloud Security" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Cloud Security (CSPM)
      </div>
      <div class="module-item" data-cat="cloud" style="display:none;" onclick="selectModule('cdr', this)">
         <img src="assets/icons/cdr.svg" alt="Cloud Detection & Response" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Cloud Detection &amp; Response (CDR)
      </div>
      <div class="module-item" data-cat="cloud" style="display:none;" onclick="selectModule('secrets', this)">
         <img src="assets/icons/key.svg" alt="Secrets Manager" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Secrets Manager
      </div>
      <div class="module-item" data-cat="workloads" style="display:none;" onclick="selectModule('cwpp', this)">
         <img src="assets/icons/shield.svg" alt="Runtime Protection" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Runtime Protection (CWPP)
      </div>
      <div class="module-item" data-cat="workloads" style="display:none;" onclick="selectModule('vmsec', this)">
         <img src="assets/icons/host.svg" alt="VM Security" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> VM Security
      </div>
      <div class="module-item" data-cat="workloads" style="display:none;" onclick="selectModule('kspm', this)">
         <img src="assets/icons/wheel.svg" alt="Kubernetes Security Posture" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Kubernetes Security Posture (KSPM)
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('ai-spm', this)">
         <img src="assets/icons/posture.svg" alt="AI-SPM" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> AI Posture (AI-SPM)
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('ai-dr', this)">
         <img src="assets/icons/ai.svg" alt="AI Detect & Respond" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Detect &amp; Respond (AI-DR)
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('agentic-ai', this)">
         <img src="assets/icons/ai.svg" alt="Agentic AI Security" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Agentic AI (ModelArmor)
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('model-dataset', this)">
         <img src="assets/icons/ai.svg" alt="AI Model & Dataset Security" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Model &amp; Dataset Security
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('red-teaming', this)">
         <img src="assets/icons/ai.svg" alt="AI Red Teaming" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Red Teaming &amp; Pen Testing
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('ai-identity', this)">
         <img src="assets/icons/user_check.svg" alt="AI Identity Security" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> AI Identity Security
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('prompt-firewall', this)">
         <img src="assets/icons/ai.svg" alt="AI Guardrails" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Guardrails (Prompt Firewall)
      </div>
      <div class="module-item" data-cat="ai" style="display:none;" onclick="selectModule('ai-grc', this)">
         <img src="assets/icons/compliance.svg" alt="AI-GRC" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Compliance (AI-GRC)
      </div>
      <div class="module-item" data-cat="compliance" style="display:none;" onclick="selectModule('comp', this)">
         <img src="assets/icons/compliance.svg" alt="Continuous Compliance" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> Continuous Compliance
      </div>
      <div class="module-item" data-cat="onprem" style="display:none;" onclick="selectModule('onprem-install', this)">
         <img src="assets/icons/onprem.svg" alt="On-Prem Deployment" width="18" height="18" style="vertical-align:middle; margin-right:6px;" /> On-Prem Deployment
      </div>
    </div>
    <div class="modules-content" id="moduleDetail">
        <div id="devsecops" class="module-detail-block">
            <div class="content-header">
                <a href="/how-to/aspm-overview/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/integrations/cicd-overview/" class="action-btn" target="_blank">Integrations</a>
                <a href="/use-cases/aspm/" class="action-btn" target="_blank">Use Case</a>
            </div>
            <div class="module-detail-title">
                DevSecOps (ASPM) <span class="agentless-badge">Agentless</span>
            </div>
            <div class="module-description">
                Embeds security practices into DevOps, automating security testing and compliance throughout the SDLC from build to runtime environments.
            </div>
            <div class="module-visual-placeholder">
                 <img src="https://accuknox.com/wp-content/uploads/ASPM2-dashboard-home.webp"  alt="DevSecOps" />
            </div>
            <a href="/use-cases/aspm/" class="learn-more-link">Learn more about DevSecOps &rarr;</a>
        </div>
        <div id="api" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/integrations/api-overview/" class="action-btn" target="_blank">Integrations</a>
                <a href="/use-cases/api-security/" class="action-btn" target="_blank">Use Case</a>
            </div>
            <div class="module-detail-title">
                API Security
            </div>
            <div class="module-description">
                Comprehensive API security monitoring and protection to detect vulnerabilities, prevent attacks, and ensure secure API communications.
            </div>
             <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/api-security.png"  alt="API Security" />
            </div>
            <a href="/use-cases/api-security/" class="learn-more-link">Learn more about API Security &rarr;</a>
        </div>
        <div id="cspm" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/high-level-onboarding/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/use-cases/cspm/" class="action-btn" target="_blank">Use Case</a>
            </div>
            <div class="module-detail-title">
                Cloud Security (CSPM) <span class="agentless-badge">Agentless</span>
            </div>
            <div class="module-description">
                Identifies cloud misconfigurations, ensures compliance, and continuously monitors security across multi-cloud environments.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/cspm.png"  alt="Cloud Security (CSPM)" />
            </div>
            <a href="/use-cases/cspm/" class="learn-more-link">Learn more about Cloud Security &rarr;</a>
        </div>
        <div id="cdr" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/getting-started/aws-cdr/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/getting-started/cdr-setup/" class="action-btn" target="_blank">Redemediation Setup</a>
                <a href="/use-cases/cdr/" class="action-btn" target="_blank">Use Case</a>
            </div>
            <div class="module-detail-title">
                Cloud Detection & Response (CDR)
            </div>
            <div class="module-description">
                Detect and remediate threats on AWS, GCP, and Azure, focusing on high-signal security events.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/CDR.png"  alt="Cloud Detection & Response (CDR)" />
            </div>
            <a href="/getting-started/aws-cdr/" class="learn-more-link">Learn more about Detection & Response &rarr;</a>
        </div>
        <div id="secrets" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/getting-started/secrets-management/" class="action-btn" target="_blank">Getting Started</a>
            </div>
            <div class="module-detail-title">
                Secrets Manager
            </div>
            <div class="module-description">
                Secure storage and management of sensitive credentials, API keys, and secrets using encryption and access controls.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/secrets-manger.png"  alt="Secrets Manager" />
            </div>
            <a href="/getting-started/secrets-management/" class="learn-more-link">Learn more about Secrets Manager &rarr;</a>
        </div>
        <div id="cwpp" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/getting-started/runtime-sec-arch/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/use-cases/cwpp/" class="action-btn" target="_blank">Use Case</a>
            </div>
            <div class="module-detail-title">
                Runtime Protection (CWPP)
            </div>
            <div class="module-description">
                Protects cloud workloads by detecting threats, vulnerabilities, and misconfigurations in real time.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/cwpp.png"  alt="Runtime Protection (CWPP)" />
            </div>
            <a href="/use-cases/cwpp/" class="learn-more-link">Learn more about Runtime Protection &rarr;</a>
        </div>
        <div id="vmsec" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/vm-security/agent-based/linux/" class="action-btn" target="_blank">Windows/Linux</a>
                <a href="/how-to/vm-security/agentless/cloud-vm-scanning/" class="action-btn" target="_blank">Cloud VMs (Agentless)</a>
                <a href="/how-to/vm-onboard-deboard-docker/" class="action-btn" target="_blank">Onboarding</a>
            </div>
            <div class="module-detail-title">
                VM Security
            </div>
            <div class="module-description">
                Protect virtual machines across Windows and Linux operating systems with vulnerability management, hardening, and runtime protection.
            </div>
            <div class="module-visual-placeholder">
                 <img src="https://help.accuknox.com/use-cases/image-15.png" alt="VM Security" />
            </div>
            <a href="https://help.accuknox.com/use-cases/vm-overview/" class="learn-more-link">Learn more about VM Security &rarr;</a>
        </div>
        <div id="kspm" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/registry-overview/" class="action-btn" target="_blank">Registry Scanning</a>
                <a href="/use-cases/kspm/" class="action-btn" target="_blank">Use Case</a>
                <a href="/use-cases/kiem/" class="action-btn" target="_blank">K8s Identity & Entitlements (KIEM)</a>
            </div>
            <div class="module-detail-title">
                Kubernetes Security Posture (KSPM)
            </div>
            <div class="module-description">
                Continuously monitors Kubernetes clusters to identify and remediate misconfigurations and vulnerabilities.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/kspm.png"  alt="KSPM" />
            </div>
            <a href="/use-cases/kspm/" class="learn-more-link">Learn more about K8s Posture &rarr;</a>
        </div>
        <div id="prompt-firewall" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/prompt-firewall/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/use-cases/prompt-firewall-overview/" class="action-btn" target="_blank">Use Case</a>
                <a href="/integrations/ai-overview/" class="action-btn" target="_blank">Integrations</a>
            </div>
            <div class="module-detail-title">
                AI Guardrails (Prompt Firewall)
            </div>
            <div class="module-description">
                Real-time inline protection for LLM apps against prompt injection, jailbreaking, sensitive-data leakage, and unsafe output.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/aiml-sec.png"  alt="AI Guardrails (Prompt Firewall)" />
            </div>
            <a href="/use-cases/prompt-firewall-overview/" class="learn-more-link">Learn more about AI Guardrails &rarr;</a>
        </div>
        <div id="red-teaming" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/aiml-custom-model-redteaming/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/use-cases/red-teaming/" class="action-btn" target="_blank">Use Case</a>
                <a href="/use-cases/subprompts-categories/" class="action-btn" target="_blank">Categories &amp; Probes</a>
            </div>
            <div class="module-detail-title">
                AI Red Teaming &amp; Pen Testing
            </div>
            <div class="module-description">
                 Automated adversarial testing to find prompt-injection, jailbreak, toxicity, and data-leak vulnerabilities in your models before deployment.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/aiml-sec.png"  alt="AI Red Teaming & Pen Testing" />
            </div>
            <a href="/use-cases/red-teaming/" class="learn-more-link">Learn more about AI Red Teaming &rarr;</a>
        </div>
        <div id="ai-dr" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/use-cases/aidr/" class="action-btn" target="_blank">Use Case</a>
                <a href="/how-to/azure-aidr/" class="action-btn" target="_blank">Azure Setup</a>
                 <a href="/support-matrix/aiml-support-matrix/" class="action-btn" target="_blank">Support Matrix</a>
            </div>
            <div class="module-detail-title">
                AI Detect &amp; Respond (AI-DR)
            </div>
            <div class="module-description">
                Continuous monitoring and response for AI security incidents and anomalies across SageMaker, Bedrock, and Azure ML.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/aiml-sec.png"  alt="AI Detect & Respond (AI-DR)" />
            </div>
            <a href="/use-cases/aidr/" class="learn-more-link">Learn more about AI-DR &rarr;</a>
        </div>
        <div id="ai-spm" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/aiml-overview/" class="action-btn" target="_blank">Getting Started</a>
                <a href="/use-cases/aiml-usecases/" class="action-btn" target="_blank">Use Cases</a>
                <a href="/support-matrix/aiml-support-matrix/" class="action-btn" target="_blank">Support Matrix</a>
            </div>
            <div class="module-detail-title">
                AI Security Posture Management (AI-SPM)
            </div>
            <div class="module-description">
                Discover AI/ML assets across cloud and on-prem, surface shadow AI, and continuously score the posture of your models, datasets, and AI applications.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/aiml-sec.png"  alt="AI Security Posture Management (AI-SPM)" />
            </div>
            <a href="/use-cases/aiml-usecases/" class="learn-more-link">Learn more about AI-SPM &rarr;</a>
        </div>
        <div id="agentic-ai" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/use-cases/modelarmor/" class="action-btn" target="_blank">Use Case</a>
                <a href="/integrations/bedrock-agentcore/" class="action-btn" target="_blank">Bedrock AgentCore</a>
                <a href="/integrations/copilot-studio/" class="action-btn" target="_blank">Copilot Studio</a>
            </div>
            <div class="module-detail-title">
                Agentic AI Security (ModelArmor)
            </div>
            <div class="module-description">
                Runtime sandboxing and zero-trust guardrails for AI agents, agent toolchains, and untrusted models using ModelArmor and KubeArmor.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/aiml-sec.png"  alt="Agentic AI Security (ModelArmor)" />
            </div>
            <a href="/use-cases/modelarmor/" class="learn-more-link">Learn more about Agentic AI Security &rarr;</a>
        </div>
        <div id="model-dataset" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/how-to/llm-static-scan/" class="action-btn" target="_blank">LLM Static Scan</a>
                <a href="/how-to/ml-static-scan/" class="action-btn" target="_blank">ML Static Scan</a>
                <a href="/use-cases/modelarmor-pickle-code/" class="action-btn" target="_blank">Use Case</a>
            </div>
            <div class="module-detail-title">
                AI Model &amp; Dataset Security
            </div>
            <div class="module-description">
                Scan models and datasets from Hugging Face, GitHub, and registries for supply-chain risks, malware, and unsafe serialization such as pickle code injection.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/aiml-sec.png"  alt="AI Model & Dataset Security" />
            </div>
            <a href="/use-cases/modelarmor-pickle-code/" class="learn-more-link">Learn more about Model &amp; Dataset Security &rarr;</a>
        </div>
        <div id="ai-identity" class="module-detail-block" style="display:none;">
            <div class="module-detail-title">
                AI Identity Security <span class="agentless-badge">Coming Soon</span>
            </div>
            <div class="module-description">
                Identity and entitlement controls for AI agents, models, and non-human identities. Coming soon.
            </div>
        </div>
        <div id="ai-grc" class="module-detail-block" style="display:none;">
            <div class="module-detail-title">
                AI Compliance &amp; Governance (AI-GRC) <span class="agentless-badge">Coming Soon</span>
            </div>
            <div class="module-description">
                Governance, risk, and compliance mapping for AI systems against frameworks like the EU AI Act, NIST AI RMF, and ISO 42001. Coming soon.
            </div>
        </div>
        <div id="comp" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="https://accuknox.com/compliance" class="action-btn" target="_blank">Compliance Support Matrix</a>
                <a href="/resources/compliance-baseline-data/" class="action-btn" target="_blank">Compliance Baseline Data</a>
                <a href="/how-to/cis-benchmarking/" class="action-btn" target="_blank">CIS Benchmarking</a>
            </div>
            <div class="module-detail-title">
                Continuous Compliance <span class="agentless-badge">Agentless</span>
            </div>
            <div class="module-description">
                Unified visibility into security posture, risk, and compliance across multi-cloud and Kubernetes environments.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/compliance.png"  alt="Continuous Compliance" />
            </div>
            <a href="/use-cases/compliance/" class="learn-more-link">Learn more about Compliance &rarr;</a>
        </div>
        <div id="onprem-install" class="module-detail-block" style="display:none;">
            <div class="content-header">
                <a href="/getting-started/on-prem-overview/" class="action-btn" target="_blank">Overview</a>
                <a href="/getting-started/on-prem-installation-guide/" class="action-btn" target="_blank">Installation Guide</a>
                <a href="/getting-started/on-prem-single-node-installation/" class="action-btn" target="_blank">Single Node Installation</a>
                <a href="/getting-started/security-on-openshift/" class="action-btn" target="_blank">Security on OpenShift</a>
                <a href="/getting-started/aws-ami/" class="action-btn" target="_blank">AWS AMI</a>
            </div>
            <div class="module-detail-title">
                On-Prem Deployment <span class="agentless-badge">Agentless</span>
            </div>
            <div class="module-description">
                Secure air-gapped deployment of the CNAPP platform designed to meet federal and regulated environment requirements.
            </div>
            <div class="module-visual-placeholder">
                 <img src="assets/images/homepage/onprem.png"  alt="On-Prem Deployment" />
            </div>
            <a href="/getting-started/on-prem-installation-guide/" class="learn-more-link">Learn more about On-Prem &rarr;</a>
        </div>
    </div>
  </div>
</section>
<section class="use-cases-section">
  <div class="section-heading-3" style="font-size: 1.8rem; font-weight: 800; text-align: center; color: #0f172a; margin-bottom: 40px;">Popular Resources & Guides</div>
  <div class="use-cases-grid">
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/shield.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Vulnerability Management</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/use-cases/epss-scoring/" target="_blank">EPSS Scoring</a></li>
         <li><a href="/use-cases/rules-engine-ticket-creation/" target="_blank">Rules Engine</a></li>
         <li><a href="/use-cases/vulnerability/" target="_blank">Vulnerability Management</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/cdr.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Cloud Detection & Response</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/use-cases/cdr/" target="_blank">CDR Overview</a></li>
         <li><a href="/getting-started/cdr-setup/" target="_blank">Alert Remediation</a></li>
         <li><a href="/getting-started/aws-cdr/" target="_blank">Onboarding</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/compliance.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Governance, Risk & Compliance</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/use-cases/compliance/" target="_blank">Multi-cloud Compliance</a></li>
         <li><a href="/use-cases/cloud-misconfigurations/" target="_blank">Drift Detection</a></li>
         <li><a href="/resources/compliance-baseline-data/" target="_blank">Compliance Baseline Data</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/cloud.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Cloud & Infrastructure Matrix</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/support-matrix/cloud-regions/" target="_blank">Cloud Regions</a></li>
         <li><a href="/support-matrix/public-cloud/" target="_blank">Public Cloud Support</a></li>
         <li><a href="/support-matrix/private-cloud/" target="_blank">Private Cloud Support</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/container.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">App Security Matrix</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/support-matrix/cicd-support-matrix/" target="_blank">CI/CD Support</a></li>
         <li><a href="/support-matrix/iac/" target="_blank">IaC Coverage</a></li>
         <li><a href="/support-matrix/registry/" target="_blank">Registry Scan Support</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/ai.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">AI & Compliance Matrix</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/support-matrix/aiml-support-matrix/" target="_blank">AI/ML Support</a></li>
         <li><a href="/support-matrix/compliance-matrix/" target="_blank">Compliance Matrix</a></li>
         <li><a href="/support-matrix/vms/" target="_blank">VM Support Matrix</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
             <img src="assets/icons/wheel.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Deployment Architectures</h3>
       </div>
       <ul class="use-case-list">
         <li><a href="/getting-started/accuknox-arch/" target="_blank">Enterprise Architecture</a></li>
         <li><a href="/getting-started/deployment-models/" target="_blank">Deployment Models</a></li>
         <li><a href="/resources/multitenancy/" target="_blank">Multi-Tenancy Support</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/eye.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Technical Resources</h3>
       </div>
       <ul class="use-case-list">
          <li><a href="/resources/accuknox-manual/" target="_blank">User Manual</a></li>
          <li><a href="/resources/cspm-troubleshooting/" target="_blank">CSPM Troubleshooting</a></li>
          <li><a href="/resources/vulnerability-database/" target="_blank">Vulnerability DB</a></li>
       </ul>
    </div>
    <div class="use-case-card">
       <div class="use-case-header">
         <div class="use-case-icon icon-blue">
            <img src="assets/icons/grid.svg" width="24" height="24" alt="" />
         </div>
         <h3 class="use-case-title">Release Notes & Updates</h3>
       </div>
       <ul class="use-case-list">
          <li><a href="/getting-started/3.4-release/" target="_blank">Latest Release (v3.4)</a></li>
          <li><a href="/getting-started/accuknox-release-notes/" target="_blank">All Release Notes</a></li>
          <li><a href="/getting-started/kubearmor-release/" target="_blank">KubeArmor Releases</a></li>
       </ul>
    </div>
  </div>
  <a href="/use-cases/" class="view-all-btn">VIEW ALL USE CASES &rarr;</a>
</section>
<section>
<div class="integrations-container">
 <div class="image-container2">
   <img src="introduction/cards/integrations-updated.png" alt="Integrations" class="integrations-image">
 </div>
 <div class="text-container-int">
   <article class="integrations-title">Integrate Seamlessly In Your Technology Ecosystem</article>
   <p class="integrations-description">Check out integrations for Azure, Google Cloud Build, AWS, Jenkins, Gitlab, CheckMarkx and more. We also support Container Platforms like Nutanix, Rafay and Mirantis and Notification platforms like Slack.</p>
   <a href="/integrations/jira-cloud/" class="btn-style">GET STARTED &rarr;</a>
 </div>
</div>
</section>

<section>
  <div class="section5-container">
    <h2 class="section-heading">Technical Support</h2>
    <div class="section5-card-container">
        <div class="section5-card">
            <img src="introduction/cards/badge1.svg" alt="Tech Support Icon">
            <h3 class="section5-card-title">Raise Ticket</h3>
            <p>Contact our Support Team to quickly resolve any issues.</p>
            <a href="https://accu-knox.atlassian.net/servicedesk/customer/portal/1" target="_blank" class="section5-card-link">CONNECT WITH US &rarr;</a>
        </div>
        <div class="section5-card">
            <img src="introduction/cards/badge2.svg" alt="Certification Icon">
            <h3 class="section5-card-title">AccuKnox Certifications</h3>
            <p>AccuKnox certifications ensure compliance with industry security standards.</p>
            <a href="https://www.accuknox.com/certifications" target="_blank" class="section5-card-link">GET CERTIFIED &rarr;</a>
        </div>
        <div class="section5-card">
            <img src="introduction/cards/badge3.svg" alt="Downloads Icon">
            <h3 class="section5-card-title">Resources</h3>
            <p>Download and make the most of AccuKnox guides and manuals.</p>
            <a href="/resources/accuknox-manual/" target="_blank" class="section5-card-link">DOWNLOAD NOW &rarr;</a>
        </div>
    </div>
  </div>
</section>

<section class="home-section-7">
<h2 class="section-heading">Find Out More</h2>
<div class="section7-nav">
    <a href="/resources/accuknox-manual/" class="section7-link" target="_blank">RESOURCES</a>
    <a href="/support-matrix/kubearmor-support-matrix/" target="_blank" class="section7-link">SUPPORT MATRIX</a>
    <a href="https://help.accuknox.com/getting-started/3.3-release/" target="_blank" class="section7-link">LATEST RELEASE NOTES</a>
    <a href="/faqs/" target="_blank" class="section7-link" style="border-right: 0px">FAQ</a>
</div>
</section>

<script>
(function() {
    // Ensure functions are available globally for onclick handlers
    window.selectCategory = function(catId, btn) {
        // 1. Update Tabs
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // 2. Filter Sidebar
        const sidebarItems = document.querySelectorAll('.module-item');
        let firstVisible = null;
        sidebarItems.forEach(item => {
            if (item.getAttribute('data-cat') === catId) {
                item.style.display = 'flex';
                if (!firstVisible) firstVisible = item;
            } else {
                item.style.display = 'none';
            }
            item.classList.remove('active');
        });

        // 3. Select first module of new category
        if (firstVisible) {
            firstVisible.click();
        }
    }

    window.selectModule = function(modId, item) {
        // 1. Update Sidebar Active State
        document.querySelectorAll('.module-item').forEach(i => i.classList.remove('active'));
        item.classList.add('active');

        // 2. Show Content
        document.querySelectorAll('.module-detail-block').forEach(b => {
            if (b.id === modId) {
                b.style.display = 'block';
            } else {
                b.style.display = 'none';
            }
        });
    }

    window.updateCarouselDisplay = function() {
        // No-op, dynamically queried now for safety
    }

    window.rotateCarousel = function(direction) {
        const cards = Array.from(document.querySelectorAll('.carousel-card'));
        if (cards.length === 0) return;

        // Identify current positions
        let leftIndex = cards.findIndex(c => c.classList.contains('card-left'));
        let centerIndex = cards.findIndex(c => c.classList.contains('card-center'));
        let rightIndex = cards.findIndex(c => c.classList.contains('card-right'));

        // Clear classes
        cards.forEach(c => c.classList.remove('card-left', 'card-center', 'card-right'));

        // Guard against missing indices
        if (leftIndex === -1 || centerIndex === -1 || rightIndex === -1) {
            // Fallback reset if state is messed up
             if (cards.length >= 3) {
                cards[0].classList.add('card-left');
                cards[1].classList.add('card-center');
                cards[2].classList.add('card-right');
             }
             return;
        }

        if (direction === 'right') {
            // Move Right item to Center. Center to Left. Left to Right (cycle)
            cards[rightIndex].classList.add('card-center');
            cards[centerIndex].classList.add('card-left');
            cards[leftIndex].classList.add('card-right');
        } else {
            // Move Left item to Center. Center to Right. Right to Left
            cards[leftIndex].classList.add('card-center');
            cards[centerIndex].classList.add('card-right');
            cards[rightIndex].classList.add('card-left');
        }
    }
})();
</script>
