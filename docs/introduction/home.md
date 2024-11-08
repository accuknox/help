---
hide:
  - navigation
  - toc
---

<style>

  .md-main__inner {
    min-width: 103% !important;
    margin-left: -2%;
    overflow-y: hidden;
    margin-top: -1%;
  }

  .md-feedback{
    display: none;
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
  padding: 50px;
}

.text-container {
  flex: 1;
}

.header1 {
  color: #fff;
  font-size: 30px;
  font-weight: 900;
  text-align: left;
  font-size: 2.5rem;
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
    width:6em;
  }

  .card h3 {
    font-size: 24px;
    margin-top: 0;
    font-weight: 300;
    margin-bottom: 12px;
  }

  .card p {
    font-size: 14px;
    color: #555;
    margin-bottom: 16px;
    text-align: center;
  }

  .card a {
    display: inline-block;
    color: #0066FF;
    text-decoration: none;
    padding: 8px 16px;
    font-size: 16px;
    transition: background-color 0.3s ease;
    font-weight: bolder;
  }

  .card a:hover {
    background-color: #f0f0f0;
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
  list-style: none;
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

  .all-use-cases {
    display: block;
    margin: 20px auto; /* centers the button */
    background-color: #0066ff; /* primary blue */
    color: white;
    padding: 10px 20px; /* adds padding */
    text-align: center;
    font-weight: bold;
    text-decoration: none;
    border: none;
    border-radius: 5px; /* optional: rounded corners */
    cursor: pointer;
  }

  .all-use-cases a {
    color: white;
    text-decoration: none;
  }

  .all-use-cases a:hover {
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
  }
}


/* SECTION 4 CSS */
.integrations-container {
  display: flex;
  align-items: center;
  background-color: #030372;
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
  font-size: xxx-large !important;
  margin-bottom: 1rem;
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

    .section5-title {
        text-align: center;
        color: #030372;
        font-size: 36px !important;
        font-weight: 900 !important;
        text-align: center;
        margin-bottom: 10px;
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
        width: 100%;
        height: 160px;
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
</style>

<!-- SECTION 1 - TOP CONTAINER -->
<section>
<div class="main-container">
  <div class="content-container">
    <div class="text-container">
      <article class="header1">Welcome to <br>AccuKnox Help Center</article>
    </div>
    <div class="image-container">
      <img src="../cards/header-img.png" alt="Help Center" style="width: 75%">
    </div>
  </div>
</div>
</section>

<!-- SECTION 2 -- SUBPRODUCT CARDS -->
<section style="background-color: #eef5fc; padding-top: 3rem;">
<article class="header2" style="margin-bottom: 1rem;">AccuKnox - Enterprise CNAPP Suite</article>
<div class="container">
  <div class="card">
    <img src="../cards/cspm.svg" alt="Cloud Security (CSPM)">
    <h3>Cloud Security (CSPM)</h3>
    <p>Identifies cloud misconfigurations, ensures compliance, and continuously monitors security across multi-cloud environments.</p>
    <a href="cspm.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/cwpp.svg" alt="Workload Protection (CWPP)">
    <h3>Workload Protection (CWPP)</h3>
    <p>Provides security for cloud workloads by detecting threats, vulnerabilities, and misconfigurations in real-time.</p>
    <a href="/getting-started/accuknox-agents/">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/aspm.svg" alt="Application Security (ASPM)">
    <h3>Application Security (ASPM)</h3>
    <p>Manages application security risks by monitoring code, configurations, and deployment pipelines for vulnerabilities.</p>
    <a href="aspm.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/devsecops.svg" alt="DevSecOps">
    <h3>DevSecOps</h3>
    <p>Embeds security practices into DevOps, automating security testing and compliance throughout the SDLC.</p>
    <a href="devsecops.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/aiml-security.svg" alt="AI/ML Security">
    <h3>AI/ML Security</h3>
    <p>The Ask Ada AI-SPM tool identifies cloud misconfigurations with continuous monitoring and real-time intelligence.</p>
    <a href="devsecops.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/open-source.svg" alt="Open Source (KubeArmor)">
    <h3>Open Source (KubeArmor)</h3>
    <p>Enforces security policies in Kubernetes clusters, offering real-time protection for containers and microservices.</p>
    <a href="devsecops.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/kiem.svg" alt="">
    <h3>Kubernetes Identity and Entitlements Management (KIEM)</h3>
    <p>Enforces IAM controls and entitlements across K8s clusters for secure authorization and to prevent privilege escalation.</p>
    <a href="kiem.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/grc.svg" style="width: 4rem;" alt="">
    <h3>Governance, Risk, and Compliance (GRC)</h3>
    <p>Provides a unified view of security posture, risk analysis, and compliance across multi-cloud and K8s environments.</p>
    <a href="grc.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>

  <div class="card">
    <img src="../cards/kspm.svg" alt="">
    <h3>Kubernetes Security Posture Management (KSPM)</h3>
    <p>Continuously monitors K8s clusters to identify and remediate misconfigurations, vulnerabilities, and threats in real-time.</p>
    <a href="kspm.md">LEARN MORE <img src="../cards/arrow.svg" style="width: 1rem; margin-bottom:-5px;"></a>
  </div>
</div>

</section>

<!-- SECTION 3 - POPULAR USE CASES -->
<section>
<div class="use-cases-container">
  <h2 class="section5-title" style="font-size: 36px; margin-top: 1rem;">Popular Use-Cases</h2>
  <div class="use-cases-grid">
    <div class="use-cases-category">
      <p class="use-cases-category-title">DevSecOps (ASPM)</p>
      <ul class="use-cases-list">
        <li><a href="#">IaC Scan AWS S3 Buckets (CI/CD Pipeline)</a></li>
        <li><a href="#">SAST + SQL Injection</a></li>
        <li><a href="#">ASPM Container Scan</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Container Security (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="#">Container Image Scan</a></li>
        <li><a href="#">Runtime Application Hardening</a></li>
        <li><a href="#">Workload Hardening</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Securing Secrets Manager (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="#">HarshiCorp Vault Hardening</a></li>
        <li><a href="#">CyberArk Conjur Hardening</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Least Permissive Posture Assessment (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="#">Runtime Application behaviour Discovery</a></li>
        <li><a href="#">Audit/Forensics</a></li>
        <li><a href="#">Zero trust Security</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Host Security (CWPP)</p>
      <ul class="use-cases-list">
        <li><a href="#">Host Scan</a></li>
        <li><a href="#">Malware Scan</a></li>
        <li><a href="#">VM Hardening</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Cloud Security (CSPM)</p>
      <ul class="use-cases-list">
        <li><a href="#">Asset Inventory</a></li>
        <li><a href="#">Cloud Misconfiguration and Drift Detection</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Automation</p>
      <ul class="use-cases-list">
        <li><a href="#">Ticketing</a></li>
        <li><a href="#">Rules Engine</a></li>
      </ul>
    </div>
    <div class="use-cases-category">
      <p class="use-cases-category-title">Prioritization</p>
      <ul class="use-cases-list">
        <li><a href="#">EPSS Scoring</a></li>
      </ul>
    </div>
  </div>
  <button class="all-use-cases">
  <a href="/use-cases/cnapp-security-overview">VIEW ALL USE CASES</a>
</button>
</div>
</section>

<!-- SECTION 4 - INTEGRATION -->
<section>
<div class="integrations-container">
 <div class="image-container2">
   <img src="../cards/integrations-circle.svg" alt="Integrations" class="integrations-image">
 </div>
 <div class="text-container">
   <article class="integrations-title">Integrations</article>
   <b class="integrations-description">Seamless Integration in your Existing Technology Ecosystem.</b>
   <p class="integrations-description">It enables automated security checks and policy enforcement throughout the development lifecycle. It enhances the security of applications by embedding security policies into the CI/CD workflow, ensuring compliance before deployment. <br>Check out integrations for Azure, Google Cloud Build, AWS, Jenkins, Gitlab, CheckMarkx and more. We also support Container Platforms like Nutanix, Rafay and Mirantis and Notification platforms like Slack. AccuKnox integrates with major SIEM and security event tools, including Splunk, AWS CloudWatch, Azure Sentinel, and leading ticketing systems like Jira, ServiceNow, and Freshservice.</p>
   <button class="get-started-button">
   <a href="#">GET STARTED</a>
   </button>
 </div>
</div>
</section>

<!-- SECTION 5 - TECHINCAL SUPPORT -->
<section>
  <div class="section5-container">
    <h2 class="section5-title">Technical Support</h2>
    <p class="section5-description">Empower your security team with the product knowledge they need to maximize the value of your solution.</p>
        <div class="section5-card-container">
            <div class="section5-card">
            <img src="../cards/badge1.svg" alt="Tech Support Icon">
            <h3 class="section5-card-title">Tech Support</h3>
            <p class="section5-card-text">Contact our Support Team to quickly resolve any issues.</p>
            <a href="#" class="section5-card-link">CONNECT WITH US &rarr;</a>
            </div>
          <div class="section5-card">
            <img src="../cards/badge2.svg" alt="Certification Icon">
            <h3 class="section5-card-title">AccuKnox Certifications</h3>
            <p class="section5-card-text">AccuKnox certifications ensure compliance with industry security standards.</p>
            <a href="#" class="section5-card-link">GET CERTIFIED &rarr;</a>
          </div>
          <div class="section5-card">
            <img src="../cards/badge3.svg" alt="Downloads Icon">
            <h3 class="section5-card-title">Downloads</h3>
            <p class="section5-card-text">Download and make the most of AccuKnox guides and manuals.</p>
            <a href="#" class="section5-card-link">DOWNLOAD NOW &rarr;</a>
          </div>
        </div>
  </div>
</section>


<!-- SECTION 6 -->
<section>
<div class="section6-container">
    <h2 class="section5-title">Product Videos & Demos</h2>

    <div class="section6-card-container">
        <!-- Card 1 -->
        <div class="section6-card">
            <div class="section6-card-image">
                <img src="placeholder-image.png" alt="Video Thumbnail">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">How to subscribe to AccuKnox from AWS Marketplace</p>
                <p class="section6-card-duration">05:24 mins</p>
            </div>
        </div>

        <!-- Card 2 -->
        <div class="section6-card">
            <div class="section6-card-image">
                <img src="placeholder-image.png" alt="Video Thumbnail">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">Product Tour | Agentless Cloud Security | Release v2.0</p>
                <p class="section6-card-duration">05:24 mins</p>
            </div>
        </div>

        <!-- Card 3 -->
        <div class="section6-card">
            <div class="section6-card-image">
                <img src="placeholder-image.png" alt="Video Thumbnail">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">AccuKnox Zero Trust Secrets Management 101</p>
                <p class="section6-card-duration">03:07 mins</p>
            </div>
        </div>

        <!-- Card 4 -->
        <div class="section6-card">
            <div class="section6-card-image">
                <img src="placeholder-image.png" alt="Video Thumbnail">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">Check and Manage Cloud Findings for AWS, GCP and Azure</p>
                <p class="section6-card-duration">Interactive Product Demo</p>
            </div>
        </div>

        <!-- Card 5 -->
        <div class="section6-card">
            <div class="section6-card-image">
                <img src="placeholder-image.png" alt="Video Thumbnail">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">How to scan GitHub IaC</p>
                <p class="section6-card-duration">Interactive Product Demo</p>
            </div>
        </div>

        <!-- Card 6 -->
        <div class="section6-card">
            <div class="section6-card-image">
                <img src="placeholder-image.png" alt="Video Thumbnail">
            </div>
            <div class="section6-card-content">
                <p class="section6-card-title">How to Prevent execution of malicious code in Jupyter Notebook</p>
                <p class="section6-card-duration">Interactive Product Demo</p>
            </div>
        </div>
    </div>

    <div class="section6-button-container">
        <a href="#" class="section6-button">MORE VIDEOS &rarr;</a>
    </div>
</div>
</section>