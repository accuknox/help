---
hide:
  - navigation
  - toc
---

<style>
/* OVERALL CSS */
  .md-main__inner {
    min-width: 103% !important;
    margin-left: -2%;
    overflow-y: hidden;
    margin-top: -1%;
  }

  .md-feedback{
    display: none;
  }


  .section-heading {
      text-align: center;
      color: #030372;
      font-size: 36px !important;
      font-weight: 900 !important;
      text-align: center;
      margin-bottom: 10px;
  }

  .btn-style a:visited {
    color: white;
  }

/* SECTION 1 CSS */
.main-container {
  background-color: #000025;
  padding: 20px 40px;
  margin-top: -0.5rem;
}

.content-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-height: 18rem;
  padding: 0px 50px;
}

.text-container {
  flex: 1;
}

.header1 {
  color: #fff;
  font-size: 30px;
  font-weight: 900;
  text-align: left;
  font-size: 2rem;
  margin-left: 2rem;
  line-height: normal;
}
.image-container {
  width: 40%;
  height: auto;
}

@media (max-width: 991px) {
  .content-container {
    flex-direction: column;
    align-items: flex-start;
    padding: 30px; /* Reduced padding for smaller screens */
  }

  .text-container {
    margin-left: 0;
    margin-bottom: 15px; /* Adjusted spacing */
    text-align: center; /* Centered text for better readability */
  }

  .header1,
  .header2 {
    font-size: 2rem; /* Adjusted font size */
    margin-left: 0; /* Reset margin for consistency */
  }

  .image-container {
    display:none;
  }
}

@media (max-width: 767px) {
  .content-container {
    padding: 20px; /* Further reduced padding */
  }

  .header1,
  .header2 {
    font-size: 1.5rem; /* Smaller font size for compact screens */
    line-height: 1.2; /* Adjusted line height */
  }

  .text-container {
    text-align: center; /* Ensures text stays centered */
  }

  .image-container {
    display:none; /* Maintain aspect ratio */
  }
}

/* SECTION 2 CSS */

    h1
    {
      display: none;
    }
.status-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: #000025; /* Tomato color for contrast */
  color: white;
  padding: 2px 6px;
  font-size: 0.7rem;
  border-radius: 3px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.header2{
      text-align: center;
      color: #030372;
      font-weight: 900 !important;
      font-size: 2rem;
      margin-bottom: 2rem;
    }

  .container {
   display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    min-width: min-content;
    margin: 0 auto;
    padding-bottom: 5rem;
    padding-left: 5rem;
    padding-right: 5rem;
  }

  .card {
        background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgb(0 0 0 / 51%);
    padding: 24px;
    text-align: center;
  }

  .card img {
    width:3.8em;
  }

  .card h3 {
    font-size: 24px;
    margin-top: 0;
    font-weight: 300;
    margin-bottom: 12px;
    font-weight: bolder;
  }

  .card p {
    font-size: 14px;
    color: #555;
    margin-bottom: 16px;
    text-align: center;
  }

  .card a {
    display: inline-block;
    color: #030372;
    text-decoration: none;
    padding: 8px 16px;
    font-size: 16px;
    transition: background-color 0.3s ease;
    font-weight: bolder;
  }

  .card a:hover {
    background-color: #f0f0f0;
    color: #030372;
  }

  @media (max-width: 991px) {
    .container {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 767px) {
    .container {
      grid-template-columns: 1fr;
      padding: 20px;
    }
  }

  /* SECTION 3 CSS */
.use-cases-container {
  padding: 40px;
}

.use-cases-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
}

.use-cases-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    column-gap: 4rem;
    row-gap: 2rem;
    padding-top: 2rem;
    padding-right: 4rem;
    padding-left: 4rem;
}

.use-cases-category {
border-top: 4px solid #0867EC;
}

.use-cases-category-title {
  font-size: 20px;
  font-weight: bold;
  color:black;
  margin-bottom: 12px;
}

.use-cases-list {
  list-style: none !important;
  padding: 0;
  margin: 0;
}

.use-cases-list li {
  list-style: square;
  font-size: 16px;
  color: #555;
  margin-bottom: 8px;
  transition: color 0.3s ease;
}

.use-cases-list li a {
  color: #007bff;
  text-decoration: none;
  transition: color 0.3s ease;
}

.use-cases-list li a:hover {
  color: #0056b3;
}

  .btn-style {
    display: block;
    margin: 20px auto; /* centers the button */
    background-color: #0066ff; /* primary blue */
    color: white !important;
    padding: 10px 20px; /* adds padding */
    text-align: center;
    font-weight: bold;
    text-decoration: none;
    border: none;
    border-radius: 5px; /* optional: rounded corners */
    cursor: pointer;
}

.btn-style:hover {
    background-color: #0056b3; /* darker blue on hover */
}

.btn-style a {
    color: white;
    text-decoration: none;
}

.btn-style a:hover {
    color: white;
    text-decoration: none;
}



@media (max-width: 991px) {
  .use-cases-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .use-cases-grid {
    grid-template-columns: 1fr;
    padding: 15px;
  }
}


/* SECTION 4 CSS */
.integrations-container {
  display: flex;
  align-items: center;
  background-color: #000025;
  padding: 100px;
}

.image-container2 {
  flex: 1;
  display: flex;
  justify-content: center;
}

.integrations-image {
  max-width: 100%;
  height: auto;
}

.text-container {
  flex: 1;
  color: #fff;
  margin-left: 40px;
}

.integrations-title {
font-weight: bold;
color: white;
font-weight: 900 !important;
font-size: xx-large;
margin-bottom: 1rem;
line-height: normal;
}

.integrations-description {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 16px;
}

.get-started-button {
    max-width: 30%;
    background-color: #0066ff;
    color: white;
    padding: 15px;
    text-align: center;
    text-decoration: none;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bolder;
  }

  .get-started-button a {
    color: white;
    text-decoration: none;
  }

  .get-started-button a:hover {
    color: white;
    text-decoration: none;
  }


@media (max-width: 991px) {
  .integrations-container {
    flex-direction: column;
    padding: 40px;
  }

  .text-container {
    margin-left: 0;
    margin-top: 20px;
  }
}


/* SECTION 5 CSS */

  .section5-container {
        background-color: #f9f9fc;
        padding: 20px;
    }


    .section5-description {
        text-align: center;
        color: #1a1a1a;
        font-size: 18px;
        margin-bottom: 40px;
        margin-top: -20px;
    }

    .section5-card-container {
        display: flex;
        justify-content: center;
        gap: 30px;
    }

    .section5-card {
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
        width: 450px;
    }

    .section5-card img {
        width: 4rem;
        /* margin-bottom: 20px; */
        margin-top: -20px;
    }

    .section5-card-title {
        color: #1a1a1a;
        font-size: 20px;
        margin-bottom: 20px;
        margin-top: 10px;
        font-weight: bold;
    }

    .section5-card-text {
        color: #1a1a1a;
        font-size: 14px;
        margin-bottom: 20px;
        padding-left: 50px;
    padding-right: 50px;
    }

    .section5-card-link {
        color: #1a73e8;
        font-size: 14px;
        text-decoration: none;
        font-weight: 600;
    }

@media (max-width: 767px) {
  .section5-card-container {
    flex-direction: column;
  }
  .section5-card {
    width: 100%;
  }
}

  /* section 6 CSS*/
 .section6-container {
        padding-left: 150px;
        padding-right: 150px;
    }

    .section6-title {
        color: #1b0b72;
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
  .section6-card-container {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      row-gap: 60px;
      justify-items: center;
  }
    .section6-card {
        width: 280px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        text-align: left;
    }

    .section6-card-image {

        background-color: #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .section6-card-content {
        padding: 15px;
    }

    .section6-card-title {
        color: #1a1a1a;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 8px;
        margin-top:0px;
    }

    .section6-card-duration {
        color: #888888;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .section6-button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .section6-button {
        padding: 10px 20px;
        font-size: 14px;
        color: #1a73e8;
        border: 2px solid #1a73e8;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
    }

    .section6-button:hover {
        background-color: #1a73e8;
        color: #ffffff;
    }

    .play-icon{
        width: 30px;
        height: 30px;
        margin-top: 80px;
        margin-left: 120px;
    }
    @media (max-width: 991px) {
      .section6-container {
        padding: 40px;
      }
      .section6-card-container {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 767px) {
      .section6-container {
        padding: 40px;
      }
      .section6-card-container {
        grid-template-columns: 1fr;
      }
    }

    /* SECTION 7 CSS*/
    .section7-container {
        padding: 20px;
    }

    .section7-nav {
        display: flex;
        gap: 5rem; /* Space between each link */
        justify-content: center; /* Center the links horizontally */

    }

    .section7-link {
        color: #0066FF; /* Blue color for text */
        text-decoration: none; /* Remove underline */
        font-weight: bold; /* Bold font style */
        font-size: 16px; /* Font size */
        padding-right: 5rem;
        border-right: 1px solid black;
    }

    .section7-link:hover {
        text-decoration: underline; /* Underline on hover */
    }

    @media (max-width: 991px) {
      .section7-nav {
        gap: 10px;
        align-items: center;
        padding: 20px;
      }
      .section7-link {
        padding-right: 20px;
      }
    }
    @media (max-width: 767px) {
      .section7-nav {
        padding: 0 30px;
        flex-direction: column;
        gap: 10px;
        align-items: normal;
      }
    }

    /* SECTION 8 CSS */
.section8-container {
    background-color: #f4f8fb;
    padding: 2rem;
}

.section8-card{
    background: white;
    padding: 2rem;
    margin: 2rem 10rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.section8-left,
.section8-right {
    flex: 1;
}

.section8-left {
    display: flex;
    justify-content: center;
    align-items: center;
}

.section8-left-image {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}

.section8-right {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.section8-right-content {
    text-align: center;
}

.section8-title {
    font-size: 1.5em;
    font-weight: bold;
    color: #000;
    margin-bottom: 8px;
}

.section8-subtitle {
    font-size: 1em;
    color: #555;
    margin-bottom: 4px;
}

.section8-cost {
    font-size: 1.25em;
    color: #e53935; /* Red color for emphasis */
    font-weight: bold;
    margin-bottom: 16px;
}

.section8-button {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.3s;
    font-weight: bolder;
}

.section8-button:hover {
    background-color: #0056b3;
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
      <img src="../cards/header-img-new.png" alt="Help Center" height="300" width="300">
    </div>
  </div>
</div>
</section>

<!-- SECTION 2 -- SUBPRODUCT CARDS -->
<section style="background-color: #eef5fc; padding-top: 2rem;">
<article class="section-heading" style="margin-bottom: 1rem;">Enterprise CNAPP Suite</article>
<div class="container">
  <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/cspm.svg" alt="Cloud Security (CSPM)" style="color: #000025">
    <h3 class="home-card-heading">Cloud Security (CSPM)</h3>
    <p>Identifies cloud misconfigurations, ensures compliance, and continuously monitors security across multi-cloud environments.</p>
    <a href="/use-cases/cspm/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px; color: #000025;"></a>
  </div>

  <div class="card" style="position: relative;">
    <img src="../cards/cwpp.svg" alt="Runtime Protection" style="color: #000025">
    <h3 class="home-card-heading">Runtime Protection (CWPP)</h3>
    <p>Provides security for cloud workloads by detecting threats, vulnerabilities, and misconfigurations in real-time.</p>
    <a href="/use-cases/cwpp/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px; color: #000025;"></a>
  </div>

 <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/aspm.svg" alt="Federal Security" style="color: #000025">
    <h3 class="home-card-heading">On-Prem Deployment for Govt/Fed Org</h3>
    <p>Secure air-gapped deployment with our CNAPP security suite to achieve federal regulatory standards. </p>
    <a href="/getting-started/on-prem-installation-guide/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;color: #000025;"></a>
  </div>

  <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/devsecops.svg" alt="DevSecOps" style="color: #000025">
    <h3 class="home-card-heading">DevSecOps (ASPM)</h3>
    <p>Embeds security practices into DevOps, automating security testing and compliance throughout the SDLC from build to runtime environments.</p>
    <a href="/use-cases/aspm/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px; color: #000025;"></a>
  </div>

  <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/aiml-security.svg" alt="AI/ML Security" style="color: #000025">
    <h3 class="home-card-heading">AI/ML Security</h3>
    <p>The AI-SPM tool identifies cloud misconfigurations with continuous monitoring and real-time intelligence.</p>
    <a href="/use-cases/jupyter-notebook/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px; color: #000025;"></a>
  </div>


  <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/kiem.svg" alt="" style="color: #000025">
    <h3 class="home-card-heading">K8s Identity & Entitlements Management (KIEM)</h3>
    <p>Enforces IAM controls and entitlements across K8s clusters for secure authorization and to prevent privilege escalation.</p>
    <a href="/use-cases/kiem/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;color: #000025;"></a>
  </div>

  <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/grc.svg" style="width: 2.5rem;" alt="" style="color: #000025">
    <h3 class="home-card-heading">Governance, Risk, and Compliance (GRC)</h3>
    <p>Provides a unified view of security posture, risk analysis, and compliance across multi-cloud and K8s environments.</p>
    <a href="/use-cases/compliance/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;color: #000025;"></a>
  </div>

  <div class="card" style="position: relative;">
    <div class="status-badge">Agentless</div>
    <img src="../cards/kspm.svg" alt="" style="color: #000025">
    <h3 class="home-card-heading">Kubernetes Security Posture Management (KSPM)</h3>
    <p>Continuously monitors K8s clusters to identify and remediate misconfigurations, vulnerabilities, and threats in real-time.</p>
    <a href="/use-cases/kspm/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;color: #000025;"></a>
  </div>


  <div class="card" style="position: relative;">
    <img src="../cards/open-source.svg" alt="Open Source (KubeArmor)" style="color: #000025">
    <h3 class="home-card-heading">Open Source -<br>KubeArmor</h3>
    <p>Enforces security policies in Kubernetes clusters, offering real-time protection for containers and microservices.</p>
    <a href="https://docs.kubearmor.io/" target="_blank">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;color: #000025;"></a>
  </div>

</div>

</section>

<!-- SECTION 3 - POPULAR USE CASES -->
<section>
<div class="use-cases-container">
  <h2 class="section-heading" style="font-size: 36px; margin-top: 1rem;">Popular Use-Cases</h2>
  <div class="use-cases-grid">
    <div class="use-cases-category">
      <p class="use-cases-category-title">DevSecOps (ASPM)</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/iac-scan/" target="_blank">IaC Scan AWS S3 Buckets (CI/CD Pipeline)</a></li>
        <li><a href="/use-cases/sast-sq/" target="_blank">SAST + SQL Injection</a></li>
        <li><a href="/use-cases/container-scan/" target="_blank">ASPM Container Scan</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Container Security (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/image-scan/" target="_blank">Container Image Scan</a></li>
        <li><a href="/use-cases/app-hardening/" target="_blank">Runtime Application Hardening</a></li>
        <li><a href="/use-cases/hardening/" target="_blank">Workload Hardening</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Securing Secrets Manager (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/hashicorp/" target="_blank">HarshiCorp Vault Hardening</a></li>
        <li><a href="/use-cases/cyberark-conjur/" target="_blank">CyberArk Conjur Hardening</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Least Permissive Posture Assessment (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/app-behavior/" target="_blank">Runtime Application Behaviour Discovery</a></li>
        <li><a href="/use-cases/forensics/" target="_blank">Audit/Forensics</a></li>
        <li><a href="/use-cases/zero-trust/" target="_blank">Zero trust Security</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Host Security (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/host-sec/" target="_blank">Host Scan</a></li>
        <li><a href="/use-cases/malware-scan/" target="_blank">Malware Scan</a></li>
        <li><a href="/use-cases/vm-hardening/" target="_blank">VM Hardening</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Cloud Security (CSPM)</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/asset-inventory/" target="_blank">Asset Inventory</a></li>
        <li><a href="/use-cases/cloud-misconfigurations" target="_blank">Cloud Misconfiguration and Drift Detection</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Automation</p>
      <ul class="use-cases-list">
        <li><a href="/integrations/freshservice-cspm/" target="_blank">Ticketing</a></li>
        <li><a href="/use-cases/rules-engine-ticket-creation/" target="_blank">Rules Engine</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Prioritization</p>
      <ul class="use-cases-list">
        <li><a href="/use-cases/epss-scoring/" target="_blank">EPSS Scoring</a></li>
      </ul>
    </div>
  </div>
  <button class="btn-style">
  <a href="/use-cases/cnapp-security-overview" target="_blank">VIEW ALL USE CASES <img src="../cards/arrow-white.svg" style="width: 1rem; margin-bottom:-5px; margin-left: 5px; color: white;"></a>
</button>
</div>
</section>

<!-- SECTION 4 - INTEGRATION -->
<section>
<div class="integrations-container">
 <div class="image-container2">
   <img src="../cards/integrations-updated.png" alt="Integrations" class="integrations-image">
 </div>
 <div class="text-container">
   <article class="integrations-title">Integrate Seamlessly In Your Technology Ecosystem</article>
   <!-- <b class="integrations-description"></b> -->
   <p class="integrations-description">Check out integrations for Azure, Google Cloud Build, AWS, Jenkins, Gitlab, CheckMarkx and more. We also support Container Platforms like Nutanix, Rafay and Mirantis and Notification platforms like Slack. AccuKnox integrates with major SIEM and security event tools, including Splunk, AWS CloudWatch, Azure Sentinel, and leading ticketing systems like Jira, ServiceNow, and Freshservice.</p>
   <button class="btn-style">
   <a href="/integrations/jira-cloud/" target="_blank">GET STARTED <img src="../cards/arrow-white.svg" style="width: 1rem; margin-bottom:-5px; margin-left: 5px; color: white;"></a>
   </button>
 </div>
</div>
</section>

<!-- SECTION 5 - TECHINCAL SUPPORT -->
<section>
  <div class="section5-container">
    <h2 class="section-heading">Technical Support</h2>
    <p class="section5-description">Empower your security team with the product knowledge they need to maximize the value of your solution.</p>
        <div class="section5-card-container">
            <div class="section5-card">
            <img src="../cards/badge1.svg" alt="Tech Support Icon">
            <h3 class="section5-card-title">Raise Ticket</h3>
            <p class="section5-card-text">Contact our Support Team to quickly resolve any issues.</p>
            <a href="https://accu-knox.atlassian.net/servicedesk/customer/portal/1" target="_blank" class="section5-card-link">CONNECT WITH US &rarr;</a>
            </div>
          <div class="section5-card">
            <img src="../cards/badge2.svg" alt="Certification Icon">
            <h3 class="section5-card-title">AccuKnox Certifications</h3>
            <p class="section5-card-text">AccuKnox certifications ensure compliance with industry security standards.</p>
            <a href="https://www.accuknox.com/certifications" target="_blank" class="section5-card-link">GET CERTIFIED &rarr;</a>
          </div>
          <div class="section5-card">
            <img src="../cards/badge3.svg" alt="Downloads Icon">
            <h3 class="section5-card-title">Resources</h3>
            <p class="section5-card-text">Download and make the most of AccuKnox guides and manuals.</p>
            <a href="/resources/accuknox-manual/" target="_blank" class="section5-card-link">DOWNLOAD NOW &rarr;</a>
          </div>
        </div>
  </div>
</section>

<!-- SECTION 6 -->
<!-- <section>
<div class="section6-container">
    <h2 class="section-heading">Product Demos</h2>
    <div class="section6-card-container">
        <div class="section6-card">
            <a href="https://www.accuknox.com/product-tour/cis-benchmarking" target="_blank">
            <div class="section6-card-image">
                <img src="../cards/1.webp" alt="">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">CIS Benchmarking (KSPM)</p>
            </div>
            </a>
        </div>
        <div class="section6-card">
        <a href="https://www.accuknox.com/product-tour/how-to-scan-github-iac" target="_blank">
            <div class="section6-card-image">
                <img src="../cards/2.webp" alt="">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">How to scan GitHub IaC (ASPM)</p>
            </div>
            </a>
        </div>
        <div class="section6-card">
        <a href="https://www.accuknox.com/product-tour/check-and-manage-cloud-findings-for-aws-gcp-and-azure" target="_blank">
            <div class="section6-card-image">
                <img src="../cards/3.webp" alt="">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">Check and Manage Cloud Findings for AWS, GCP and Azure (CSPM)</p>
            </div>
            </a>
        </div>
        <div class="section6-card">
        <a href="https://www.accuknox.com/product-tour/protect-cve-2024-3094-xz-liblzma-backdoor-attacks" target="_blank">
            <div class="section6-card-image">
                <img src="../cards/4.webp" alt="">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">Protect CVE-2024-3094 XZ/liblzma Backdoor Attacks (CWPP)</p>
            </div>
            </a>
        </div>
        <div class="section6-card">
           <a href="https://www.accuknox.com/product-tour/how-to-prevent-execution-of-malicious-code-in-jupyter-notebook" target="_blank">
            <div class="section6-card-image">
                <img src="../cards/5.webp" alt="">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">Prevent execution of malicious code in Jupyter Notebook (AI/ML Security)</p>
            </div>
            </a>
        </div>
        <div class="section6-card">
            <a href="https://www.accuknox.com/product-tour/how-to-create-a-remediation-ticket-using-jira" target="_blank">
            <div class="section6-card-image">
                <img src="../cards/6.webp" alt="">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">How to Create a Remediation Ticket Using JIRA</p>
            </div>
            </a>
        </div>
    </div>
<button class="btn-style">
  <a href="https://www.youtube.com/@accuknox" target="_blank">MORE VIDEOS <img src="../cards/arrow-white.svg" style="width: 1rem; margin-bottom:-5px; margin-left: 5px; color: white;"></a></a>
</button>
</div>
</section> -->


<!-- SECTION 7  - -->
<section style="padding-top: 2rem; padding-bottom: 2rem;" class="home-section-7">
<h2 class="section-heading" style="margin-bottom: 1.6em;">Find Out More</h2>
<div class="section7-nav">
    <a href="/resources/accuknox-manual/" class="section7-link" target="_blank">RESOURCES</a>
    <a href="/support-matrix/kubearmor-support-matrix/" target="_blank" class="section7-link">SUPPORT MATRIX</a>
    <a href="/getting-started/2.1-2.2-release/" target="_blank" class="section7-link">LATEST RELEASE NOTES</a>
    <a href="/faqs/" target="_blank" class="section7-link" style="border-right: 0px">FAQ</a>
</div>
</section>

<!-- SECTION 8  -->
<!-- <section class="section8-container" style="margin-bottom: -1rem">
    <div class="section8-card">
    <div class="section8-left">
        <img src="../cards/s8-image-left.png" alt="Why AccuKnox?" class="section8-left-image">
    </div>
    <div class="section8-right">
        <div class="section8-right-content">
            <img src="../cards/s8-image-right.png" alt="Why AccuKnox?" class="section8-left-image"><br><br>
            <button class="section8-button">SCHEDULE A DEMO</button>
        </div>
    </div>
    </div>
</section> -->
