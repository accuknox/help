---
title: Sample Report Templates
description: Explore Accuknox's sample report templates for various security and compliance categories - ASPM, CSPM, CWPP, KSPM.
hide:
  - toc
---

# Sample Report Templates

Through AccuKnox platform, you can generate various security and compliance reports for your cloud infrastructure and applications. These reports provide insights into vulnerabilities, misconfigurations, compliance status, and overall security posture.

!!! note
    These reports can be scheduled or on-demand and can be configured from [Settings > Reports](https://app.accuknox.com/reports)

    You can view all generated reports from [File Manager](https://app.accuknox.com/file-manager)

<div class="grid-cards">
  <a class="card" href="../assets/CSPM_Report.pdf" target="_blank">
    <div class="card-content">
      <h3>CSPM (Cloud Misconfiguration)</h3>
      <p class="card-action">Sample Report <span>&rarr;</span></p>
    </div>
  </a>
  <a class="card" href="../assets/Cloud_Compliance_Report.pdf" target="_blank">
    <div class="card-content">
      <h3>Cloud Compliance</h3>
      <p class="card-action">Sample Report <span>&rarr;</span></p>
    </div>
  </a>
  <a class="card" href="../assets/ASPM_Report.pdf" target="_blank">
    <div class="card-content">
      <h3>ASPM</h3>
      <p class="card-action">Sample Report <span>&rarr;</span></p>
    </div>
  </a>

  <a class="card" href="../assets/MS365_CIS_Report.pdf" target="_blank">
    <div class="card-content">
      <h3>Microsoft 365 CIS Benchmark</h3>
      <p class="card-action">Sample Report <span>&rarr;</span></p>
    </div>
  </a>

  <a class="card" href="../assets/AISPM_Report.pdf" target="_blank">
    <div class="card-content">
      <h3>AI Red Teaming</h3>
      <p class="card-action">Sample Report <span>&rarr;</span></p>
    </div>
  </a>

  <div class="card disabled">
    <div class="card-content">
      <h3>CWPP</h3>
      <p>Sample Report will be available soon</p>
    </div>
  </div>

  <div class="card disabled">
    <div class="card-content">
      <h3>DAST Scan</h3>
      <p>Sample Report will be available soon</p>
    </div>
  </div>
</div>


You can also export all the findings from the AccuKnox platform in CSV format for further analysis. To export findings, navigate to the respective module (e.g., Vulnerability Management, Compliance) and look for the export option.

<style>
.grid-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 24px;
  margin-top: 24px;
}

.card {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 12px;
  text-decoration: none !important;
  color: inherit !important;
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  background: var(--md-default-bg-color);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  height: 100%;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  border-color: var(--md-primary-fg-color);
}

.card.disabled {
  opacity: 0.7;
  cursor: not-allowed;
  pointer-events: none;
  background-color: var(--md-default-bg-color--light);
  border-style: dashed;
  box-shadow: none;
}

.card-content {
  padding: 24px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  justify-content: space-between;
  text-align: center;
}

.card-content h3 {
  margin: 0 0 16px 0;
  color: var(--md-primary-fg-color);
  font-weight: 700;
  font-size: 1.1rem;
}

.card-action {
  margin: 0;
  font-weight: 600;
  color: var(--md-primary-fg-color);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: gap 0.2s ease;
}

.card:hover .card-action {
  gap: 12px;
}

.card-content p {
  margin: 0;
  font-size: 0.9em;
  color: var(--md-default-fg-color--light);
}
</style>
