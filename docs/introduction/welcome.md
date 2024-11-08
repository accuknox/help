---
hide:
  - navigation
  - toc
---

<style>

  .md-main__inner {
    min-width: 95% !important;
  }
  /* SECTION 1 CSS */
.main-container {
  background-color: #000080;
  padding: 40px;
}

.content-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-height: 18rem;
}

.text-container {
  flex: 1;
}

.header1 {
  color: #fff;
  font-size: 36px;
  font-weight: 900;
  text-align: left;
  font-size: 2.5rem;
  line-height: normal;
}

.image-container {
  width: 50%;
  height: 400px;
}

@media (max-width: 991px) {
  .content-container {
    flex-direction: column;
    align-items: stretch;
  }

  .text-container {
    margin-right: 0;
    margin-bottom: 20px;
  }

  .image-container {
    width: 100%;
    height: 300px;
  }
}

@media (max-width: 767px) {
  .image-container {
    height: 200px;
  }
}

/* SECTION 2 CSS */

    h1
    {
      display: none;
    }

.header2{
      text-align: center;
      color: #030372;
      font-weight: 900 !important;
      font-size: xxx-large;
      margin-bottom: 1rem;
    }

  .container {
   display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    min-width: min-content;
    margin: 0 auto;
  }

  .card {
        background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgb(0 0 0 / 51%);
    padding: 24px;
    text-align: center;
  }

  .card img {
    width: 8em;
  }

  .card h3 {
    font-size: 24px;
    margin-top: 0;
    font-weight: 600;
    margin-bottom: 12px;
  }

  .card p {
    font-size: 14px;
    color: #555;
    margin-bottom: 16px;
    text-align: left;
  }

  .card a {
    display: inline-block;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-size: 14px;
    transition: background-color 0.3s ease;
  }

  .card a:hover {
    background-color: #0056b3;
  }

  @media (max-width: 991px) {
    .container {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 767px) {
    .container {
      grid-template-columns: 1fr;
    }
  }
</style>

<!-- SECTION 1 - TOP CONTAINER -->
<section>
<div class="main-container">
  <div class="content-container">
    <div class="text-container">
      <article class="header1">Welcome to AccuKnox Help Center</article>
    </div>
    <div class="image-container">
      <img src="../cards/header-img.png" alt="Help Center" style="width: 75%">
    </div>
  </div>
</div>
</section>

<!-- SECTION 2 -- SUBPRODUCT CARDS -->
<section style="background-color: #eef5fc; padding-top: 3rem;">
<article class="header2">AccuKnox - Enterprise CNAPP Suite</article>
<div class="container">
  <div class="card">
    <img src="../cards/cspm.svg" alt="Cloud Security (CSPM)">
    <h3>Cloud Security (CSPM)</h3>
    <p>Identifies cloud misconfigurations, ensures compliance, and continuously monitors security across multi-cloud environments.</p>
    <a href="cspm.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/cwpp.svg" alt="Workload Protection (CWPP)">
    <h3>Workload Protection (CWPP)</h3>
    <p>Provides security for cloud workloads by detecting threats, vulnerabilities, and misconfigurations in real-time.</p>
    <a href="/getting-started/accuknox-agents/">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/aspm.svg" alt="Application Security (ASPM)">
    <h3>Application Security (ASPM)</h3>
    <p>Manages application security risks by monitoring code, configurations, and deployment pipelines for vulnerabilities and threats.</p>
    <a href="aspm.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/devsecops.svg" alt="DevSecOps">
    <h3>DevSecOps</h3>
    <p>Embeds security practices into DevOps, automating security testing and compliance throughout the software development lifecycle.</p>
    <a href="devsecops.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/aiml-security.svg" alt="AI/ML Security">
    <h3>AI/ML Security</h3>
    <p>Ask Ada, the AI-SPM tool from AccuKnox identifies cloud misconfigurations with continuous monitoring and real-time intelligence, ensuring secure compliance.</p>
    <a href="devsecops.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/open-source.svg" alt="Open Source (KubeArmor)">
    <h3>Open Source (KubeArmor)</h3>
    <p>Enforces security policies in Kubernetes clusters, offering real-time protection for containers and microservices environments.</p>
    <a href="devsecops.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/kiem.svg" alt="">
    <h3>Kubernetes Identity and Entitlements Management (KIEM)</h3>
    <p>Enforces identity-based access controls and entitlements across Kubernetes clusters to ensure secure authorization and prevent privilege escalation.</p>
    <a href="kiem.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/grc.svg" alt="">
    <h3>Governance, Risk, and Compliance (GRC)</h3>
    <p>Provides a unified view of security posture, risk analysis, and compliance across multi-cloud and Kubernetes environments.</p>
    <a href="grc.md">Learn More</a>
  </div>

  <div class="card">
    <img src="../cards/kspm.svg" alt="">
    <h3>Kubernetes Security Posture Management (KSPM)</h3>
    <p>Continuously monitors Kubernetes clusters to identify and remediate misconfigurations, vulnerabilities, and threats in real-time.</p>
    <a href="kspm.md">Learn More</a>
  </div>

</div>
</section>
