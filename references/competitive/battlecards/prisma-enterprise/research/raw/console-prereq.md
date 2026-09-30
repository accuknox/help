> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/get-started/console-prerequisites.md).

# Prisma Cloud Console Prerequisites

Allow the following IP addresses and hostnames, used by the different components that comprise Prisma Cloud to ensure contiuned connectivity and monitoring of your cloud environments.

* [NAT Gateway IP Addresses for Prisma Cloud](#idcb6d3cd4-d1bf-450a-b0ec-41c23a4d4280)
* [Prisma Cloud Administrative Console](#id82dc870f-ce5b-45c9-a196-f4d069cf94a2)
* [Whitelist IPs for Transporter and Application Security Integrations](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/application-security/manage-network-tunnel/manage-network-tunnel.md#whitelist-ip-addresses)

## NAT Gateway IP Addresses for Prisma Cloud

Prisma® Cloud uses the following NAT gateway IP addresses. To ensure that you can access Prisma Cloud and the API for any integrations that you enabled between Prisma Cloud and your incidence response workflows, or your agentless deployment or the Prisma Cloud Defenders to communicate with the Prisma Cloud Compute Console, review the list and update the IP addresses in your allow lists.

In the event of disruption due to a disaster, to help backup data in a timely manner, add the Disaster Recovery (DR) IP addresses to your allow lists.

To add these IP addresses to an allow list, you may need to work with your network security team. The configuration for where you set up the allow list is dependent on your network architecture and it could be your firewall, proxy, or the server itself.

* The Prisma Cloud URL indicates the region where your tenant is deployed. For example, your tenant is on app3 if your URL is <https://app3.prismacloud.io/>.
* On the **Runtime Security > Manage > System > Utilities**, find the region in the URL for **Path to Console**. Use that region to identify the destination IP address, which you must allow or add as trusted to access the Prisma Cloud Compute console. For example, if the URL is <https://us-west1.cloud.twistlock.com/us-xxxxxx>, **us-west1** indicates your Compute console region.

Use the table below to review the IP addresses to allow: **Egress**-From Defenders to Console; **Ingress**-From Console in to your environment.

On app3, which is <https://app3.prismacloud.io/> for example, will need an outbound security rule for the Egress IP address `34.82.51.12`. Compute requires only an outbound rule to Console for Agentless and Defender deployments communications. For sending alerts to your environment, you’d add an inbound security rule to the Ingress IP address `104.198.109.73`.

To install Prisma Cloud Defenders in Kubernetes cluster, in addition to being able to connect to the Prisma Cloud Compute Console, the nodes in your cluster must be able to access the Prisma Cloud cloud registry at registry-auth.twistlock.com.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-59e36483f36a080fc2d3b56207f3cf65e6e1c573%2Faccess-pc-visualization.png?alt=media" alt="access pc visualization"><figcaption></figcaption></figure>

| Prisma Cloud URL (AWS Region)                                   | Source IP Address to Allow (Ingress)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Compute SaaS Console Region (GCP)                                                                                                                                                                                                            | DR IP Address to Allow                                                                                                                                                                               |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **app.prismacloud.io** us-east-1 (N.Virginia)                   | <p>3.210.133.47</p><p>3.214.145.192</p><p>3.210.87.2</p><p>34.235.13.250</p><p>44.207.239.90</p><p>3.217.51.44</p><p>3.218.144.244</p><p>18.213.96.188</p><p>34.195.27.46</p><p>34.199.10.120</p><p>34.205.176.82</p><p>34.228.96.118</p><p>52.201.19.205</p><p>52.2.58.117</p><p>54.147.35.106</p><p>54.144.58.175</p><p>54.147.35.106</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>54.147.35.106</li><li>3.210.87.2</li></ul>                                                                                    | <p><strong>us-east1 (South Carolina)</strong></p><p>Egress: 34.75.54.101</p><p>Ingress: 34.74.84.51, 34.139.64.150, 34.139.249.192, 34.23.229.147, 34.74.93.165, 35.185.127.202</p>                                                          | <p>52.25.108.159/32</p><p>34.213.129.111/32</p><p>44.242.81.208/32</p><p>52.40.100.6/32</p><p>54.71.172.241/32</p><p>44.236.217.120/32</p>                                                           |
| **app2.prismacloud.io** us-east-2 (Ohio)                        | <p>3.136.199.10</p><p>3.16.7.30</p><p>3.132.209.81</p><p>3.22.252.89</p><p>3.139.149.174</p><p>3.132.120.136</p><p>3.18.252.111</p><p>13.59.164.228</p><p>18.191.115.70</p><p>18.218.243.39</p><p>18.221.72.80</p><p>18.223.141.221</p><p>18.116.185.157</p><p>18.223.154.151</p><p>18.225.3.219</p><p>18.117.28.137</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>3.139.149.174</li><li>3.132.209.81</li></ul>                                                                                                     | <p><strong>us-east1 (South Carolina)</strong></p><p>Egress: 34.75.54.101</p><p>Ingress: 34.74.84.51, 34.139.64.150, 34.139.249.192, 34.23.229.147, 34.74.93.165, 35.185.127.202</p>                                                          | <p>54.176.152.228/32</p><p>54.193.231.56/32</p><p>54.219.105.0/32</p><p>52.8.73.14/32</p><p>52.52.91.251/32</p><p>54.215.34.77/32</p>                                                                |
| **app3.prismacloud.io** us-west-2 (Oregon)                      | <p>44.233.39.196</p><p>52.12.85.11</p><p>54.70.207.107</p><p>34.208.190.79</p><p>52.24.59.168</p><p>52.39.60.41</p><p>52.26.142.61</p><p>54.213.143.171</p><p>54.218.131.166</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>52.35.163.8</li><li>44.231.203.74</li><li>44.231.142.62</li></ul>                                                                                                                                                                                                                        | <p><strong>us-west1 (Oregon)</strong></p><p>Egress: 34.82.51.12</p><p>Ingress: 34.82.138.152, 35.230.69.118, 104.198.109.73, 34.19.57.46, 34.83.186.93, 34.168.3.165</p>                                                                     | <p>34.192.147.35/32</p><p>34.205.10.23/32</p><p>54.221.206.73/32</p><p>54.145.56.75/32</p><p>54.152.99.85/32</p><p>52.73.209.182/32</p>                                                              |
| **app4.prismacloud.io** us-west-1 (N.California)                | <p>13.52.27.189</p><p>13.52.105.217</p><p>13.52.157.154</p><p>13.52.175.228</p><p>50.18.198.235</p><p>50.18.117.136</p><p>52.52.58.18</p><p>52.52.50.152</p><p>52.52.110.223</p><p>52.52.197.213</p><p>52.53.67.144</p><p>54.153.31.13</p><p>54.193.251.180</p><p>54.241.31.130</p><p>54.215.44.246</p><p>184.72.47.199</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>50.18.117.136</li><li>54.215.44.246</li></ul>                                                                                                 | <p><strong>us-west1 (Oregon)</strong></p><p>Egress: 34.82.51.12</p><p>Ingress: 34.82.138.152, 35.230.69.118, 104.198.109.73, 34.19.57.46, 34.83.186.93, 34.168.3.165</p>                                                                     | <p>3.18.55.196/32</p><p>3.18.59.163/32</p><p>3.141.248.48/32</p><p>3.135.129.242/32</p><p>3.22.165.22/32</p><p>3.141.146.82/32</p>                                                                   |
| **app5.prismacloud.io** us-east-2 (Ohio)                        | <p>3.128.141.242</p><p>3.129.241.104</p><p>3.130.104.173</p><p>3.136.191.187</p><p>13.59.109.178</p><p>18.190.115.80</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | <p><strong>us-east1 (South Carolina)</strong></p><p>Egress: 34.75.54.101</p><p>Ingress: 34.74.84.51, 34.139.64.150, 34.139.249.192, 34.23.229.147, 34.74.93.165, 35.185.127.202</p>                                                          |                                                                                                                                                                                                      |
| **app.anz.prismacloud.io** ap-southeast-2 (Sydney)              | <p>3.104.84.8</p><p>3.105.224.202</p><p>54.66.162.181</p><p>3.104.252.91</p><p>13.210.254.18</p><p>13.239.110.68</p><p>13.55.65.214</p><p>13.211.114.167</p><p>13.237.94.143</p><p>52.62.75.140</p><p>52.62.194.176</p><p>52.65.17.104</p><p>52.64.90.100</p><p>54.66.215.148</p><p>54.79.91.7</p><p>54.206.227.53</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>52.64.90.100</li><li>54.206.227.53</li></ul>                                                                                                       | <p><strong>asia-northeast1 (Tokyo, Japan)</strong> or <strong>australia-southeast1 (Sydney, Australia)</strong></p><p>Egress: 35.194.113.255, 35.244.121.190</p><p>Ingress: 35.200.123.236, 35.189.44.184, 34.116.88.189, 35.189.14.189,</p> | <p>18.176.206.56</p><p>35.79.185.43</p><p>35.79.234.190</p><p>35.79.203.12</p><p>54.64.241.193</p><p>54.178.36.219</p><p>54.64.112.185</p>                                                           |
| **app.ca.prismacloud.io** ca-central-1 (Canada - Central)       | <p>3.97.19.141</p><p>3.97.195.202</p><p>3.97.251.220</p><p>3.97.225.213</p><p>3.99.103.226</p><p>3.98.226.37</p><p>3.96.232.79</p><p>3.98.207.92</p><p>3.99.103.226</p><p>15.223.59.158</p><p>15.223.96.201</p><p>15.223.127.111</p><p>52.60.127.179</p><p>99.79.30.121</p><p>35.182.209.121</p><p>35.183.55.7</p><p>35.182.155.223</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>35.183.55.7</li><li>3.98.207.92</li></ul>                                                                                         | <p><strong>northamerica-northeast1 (Montréal, Québec)</strong></p><p>Egress: 35.203.59.190</p><p>Ingress: 35.203.31.67, 34.118.176.160, 34.47.2.35</p>                                                                                       | -                                                                                                                                                                                                    |
| **app.prismacloud.cn** cn-northwest-1 (Ningxia)                 | <p>52.82.89.61</p><p>52.82.102.153</p><p>52.82.104.173</p><p>52.83.179.1</p><p>52.83.70.13</p><p>52.83.77.73</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Compute SaaS not supported                                                                                                                                                                                                                   | -                                                                                                                                                                                                    |
| **app.ind.prismacloud.io**                                      | <p>13.126.142.108</p><p>3.108.78.191</p><p>65.0.233.228</p><p>15.207.175.101</p><p>15.207.56.212</p><p>3.108.163.21</p><p>3.109.149.80</p><p>35.154.114.39</p><p>65.1.154.7</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>65.0.226.192</li><li>13.127.213.101</li></ul>                                                                                                                                                                                                                                             | <p><strong>asia-south1 (Mumbai)</strong></p><p>Egress: 35.200.249.161</p><p>Ingress: 35.200.140.118, 34.93.124.157, 34.47.154.73</p>                                                                                                         | <p>3.109.168.12</p><p>3.111.190.7</p><p>13.127.213.101</p><p>13.126.158.102</p><p>15.206.136.14</p><p>43.204.57.225</p><p>65.0.226.192</p>                                                           |
| **app.id.prismacloud.io** ap-southeast-3 (Jakarta)              | <p>43.218.52.184/32</p><p>43.218.204.143/32</p><p>108.136.123.215/32</p><p>108.137.193.28/32</p><p>43.218.206.19/32</p><p>43.218.206.239/32</p><p>16.78.11.15/32</p><p>16.78.25.100/32</p><p>43.218.192.76/32</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>13.248.253.230</li><li>3.33.202.249</li></ul>                                                                                                                                                                                                           | <p><strong>asia-southeast2 (Jakarta)</strong></p><p>Egress: 34.101.179.78, 34.101.75.225, 34.101.158.55</p><p>Ingress: 34.101.121.138</p>                                                                                                    | -                                                                                                                                                                                                    |
| **app.uk.prismacloud.io** eu-west2 (London)                     | <p>13.42.159.205</p><p>3.8.248.150</p><p>35.176.28.215</p><p>3.9.200.0</p><p>18.133.126.85</p><p>18.134.251.157</p><p>18.168.9.241</p><p>18.168.51.89</p><p>35.176.57.39</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>3.9.243.250</li><li>18.133.59.44</li></ul>                                                                                                                                                                                                                                                   | <p><strong>europe-west2 (UK)</strong></p><p>Egress: 34.105.197.208</p><p>Ingress: 34.89.87.128, 34.142.29.59, 34.89.33.47</p>                                                                                                                | -                                                                                                                                                                                                    |
| **app.eu.prismacloud.io** eu-central-1 (Frankfurt)              | <p>3.69.215.10</p><p>3.73.209.143</p><p>3.75.34.63</p><p>3.76.108.18</p><p>3.121.64.255</p><p>3.121.248.165</p><p>3.121.107.154</p><p>3.123.89.253</p><p>3.126.35.83</p><p>3.126.161.46</p><p>18.184.105.224</p><p>18.185.81.104</p><p>18.184.42.114</p><p>18.198.33.246</p><p>18.198.74.25</p><p>18.159.139.221</p><p>18.192.97.20</p><p>52.29.141.235</p><p>52.58.36.219</p><p>52.211.138.79/32</p><p>52.208.61.249/32</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>3.69.215.10</li><li>18.159.139.221</li></ul> | <p><strong>europe-west3 (Frankfurt, Germany)</strong></p><p>Egress: 34.107.65.220</p><p>Ingress: 34.107.91.105, 35.198.174.6, 34.141.93.246, 34.141.89.174, 34.141.2.56, 35.198.185.51, 34.247.199.145/32</p>                                | <p>3.65.146.60/32</p><p>3.65.81.38/32</p><p>3.65.16.200/32</p><p>3.65.81.86/32</p><p>3.248.43.139/32</p><p>54.73.199.140/32</p><p>52.209.24.141/32</p><p>18.198.160.165/32</p><p>18.194.43.28/32</p> |
| **app2.eu.prismacloud.io** eu-west-1 (Ireland)                  | <p>52.208.88.215</p><p>54.170.230.172</p><p>54.72.135.50</p><p>18.200.200.125</p><p>3.248.26.245</p><p>99.81.226.57</p><p>52.208.244.121</p><p>18.200.207.86</p><p>63.32.161.197</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>54.170.182.84</li><li>79.125.19.221</li></ul>                                                                                                                                                                                                                                        | <p><strong>europe-west2 (UK)</strong></p><p>Egress: 34.105.197.208</p><p>Ingress: 34.89.87.128, 34.142.29.59, 34.89.33.47</p>                                                                                                                | <p>18.135.53.56</p><p>3.9.243.250</p><p>18.170.22.143</p><p>18.133.59.44</p><p>18.170.145.42</p><p>18.134.51.101</p><p>18.170.187.88</p>                                                             |
| **app.fr.prismacloud.io** eu-west-3 (Paris)                     | <p>13.37.138.49</p><p>13.37.20.19</p><p>13.39.40.33</p><p>13.37.126.150</p><p>13.38.189.211</p><p>13.36.26.86</p><p>15.236.58.164</p><p>15.188.106.72</p><p>15.188.116.74</p><p>15.188.46.120</p><p>15.188.209.236</p><p>15.188.0.67</p><p>35.181.110.153</p><p>35.180.236.144</p><p>52.47.148.170</p><p>52.47.117.46</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>35.180.236.144</li><li>52.47.148.170</li></ul>                                                                                                  | <p><strong>europe-west9 (Paris, France)</strong></p><p>Egress: 34.163.33.98</p><p>Ingress: 34.163.186.175, 34.163.241.103, 34.163.12.56</p>                                                                                                  | -                                                                                                                                                                                                    |
| **app.gov.prismacloud.io** us-gov-west-1 (AWS GovCloud US-West) | <p>3.32.253.13</p><p>3.30.72.123</p><p>3.32.126.62</p><p>15.200.146.166</p><p>15.200.89.211</p><p>44.231.203.74</p><p>44.231.142.62</p><p>52.35.163.8</p><p>52.35.163.8</p>                                                                                                                                                                                                                                                                                                                                                                                                                                             | <p><strong>us-west1 (Oregon)</strong></p><p>Egress: 34.82.51.12, 35.230.86.130</p><p>Ingress: 34.82.138.152, 35.230.69.118, 104.198.109.73, 34.19.57.46, 34.83.186.93, 34.168.3.165</p>                                                      |                                                                                                                                                                                                      |
| **app.jp.prismacloud.io** ap-northeast-1 (Tokyo)                | <p>18.178.170.193</p><p>18.182.113.156</p><p>3.114.23.157</p><p>13.114.192.248</p><p>13.230.74.246</p><p>18.180.127.96</p><p>35.75.84.20</p><p>35.76.22.242</p><p>54.249.107.1</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>35.79.185.43</li><li>54.178.36.219</li></ul>                                                                                                                                                                                                                                           | <p><strong>asia-northeast1 (Tokyo, Japan, APAC)</strong></p><p>Egress: 35.194.113.255</p><p>Ingress: 35.200.123.236, 35.187.195.198, 34.85.99.145</p>                                                                                        | -                                                                                                                                                                                                    |
| **app.sg.prismacloud.io** ap-southeast-1 (Singapore)            | <p>3.0.37.2</p><p>13.250.152.72</p><p>13.251.200.128</p><p>13.250.248.219</p><p>13.229.192.152</p><p>18.136.72.0</p><p>18.139.106.36</p><p>18.142.98.147</p><p>18.139.183.196</p><p>18.136.115.165</p><p>52.76.28.40</p><p>52.76.70.227</p><p>52.221.36.124</p><p>52.221.157.53</p><p>52.76.202.193</p><p>52.76.80.172</p><p>54.251.48.202</p><p>54.179.51.255</p><p>122.248.219.240</p><p>Required for Transporter and Application Security integrations with network restrictions, such as self-hosted code environments.</p><ul><li>3.0.37.2</li><li>54.251.48.202</li></ul>                                         | <p><strong>asia-southeast1 (Singapore)</strong></p><p>Egress: 35.198.194.238</p><p>Ingress: 34.87.137.141, 35.186.153.185, 34.87.100.14</p>                                                                                                  | -                                                                                                                                                                                                    |
| **Data Security on Prisma Cloud US**                            | <p>3.128.230.117</p><p>3.14.212.156</p><p>3.22.23.119</p><p>20.9.80.30</p><p>20.9.81.254</p><p>20.228.128.132</p><p>20.228.250.145</p><p>20.253.198.116</p><p>20.253.198.147</p>                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                              |                                                                                                                                                                                                      |
| **Data Security on Prisma Cloud EU**                            | <p>3.64.66.135</p><p>18.198.52.216</p><p>3.127.191.112</p><p>20.223.237.240</p><p>20.238.97.44</p><p>20.26.194.122</p><p>51.142.252.210</p><p>51.124.198.75</p><p>51.124.199.134</p>                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                              |                                                                                                                                                                                                      |

Due to compliance reasons, backup/Disaster Recovery (DR) IP addresses are not supported in some regions.

## Prisma Cloud Administrative Console

Allow access to the following domains, to use the Prisma Cloud user interface:

* Palo Alto Networks sub domains.

  You can add \*.paloaltonetworks.com to include all of the following URLs:

  * apps.paloaltonetworks.com
  * autofocus.paloaltonetworks.com
  * docs.paloaltonetworks.com
  * identity.paloaltonetworks.com
  * live.paloaltonetworks.com
  * login.paloaltonetworks.com
  * support.paloaltonetworks.com

    Some additional URLs are also required for the Prisma Cloud Administrative Console.
* Prisma Cloud tenant URL

  The URL for Prisma Cloud varies depending on the region and cluster on which your tenant is deployed. Your welcome email will include one of the following URLs that is specific to the tenant provisioned for you:

  * <https://app.prismacloud.io>
  * <https://app2.prismacloud.io>
  * <https://app3.prismacloud.io>
  * <https://app4.prismacloud.io>
  * <https://app5.prismacloud.io>
  * <https://app.anz.prismacloud.io>
  * <https://app.ca.prismacloud.io>
  * <https://app.eu.prismacloud.io>
  * <https://app2.eu.prismacloud.io>
  * <https://app.fr.prismacloud.io>
  * <https://app.gov.prismacloud.io>
  * <https://app.ind.prismacloud.io>
  * <https://app.id.prismacloud.io>
  * <https://app.jp.prismacloud.io>
  * <https://app.sg.prismacloud.io>
  * <https://app.prismacloud.cn>
  * <https://app.uk.prismacloud.io>

    Make sure you whitelist **\*.network.prismacloud.io** in order for your RQL Network queries to work.
* Prisma Cloud API interface

  api\*.\*.prismacloud.io. See [API URLs](https://pan.dev/prisma-cloud/api/cspm/api-urls/) for your Prisma Cloud tenant.
* URLs associated with the sign-in and status updates for Prisma Cloud
  * assets.adobedtm.com
  * cloudfront.net
  * dpm.demdex.net
  * google.com
  * google.com/recaptcha/
  * gstatic.com
  * gstatic.com/recaptcha/
  * polyfill.io
* wss\://\*.prismacloud.io
* Cloud Workload Protection (CWP) capabilities

  \*.twistlock.com, for access to the CWP capabilities available on the **Compute** tab on the Prisma Cloud console.
* Cloud Network Security (CNS) /Microsegmentation capabilities

  \*.network.prismacloud.io, for access to the Microsegmentation capabilities that are enabled on the **Network Security** tab on the Prisma Cloud console.
* Application Security capabilities
  * \*.bridgecrew\.cloud, for the Application Security capabilities that are enabled on the Application Security and Settings tab on the Prisma Cloud console. Ensure that you’ve selected Application Security in the Prisma Cloud switcher to access the customized navigation for Application Secturity. The Application Security Configuration is under Settings.
* When using Checkov to scan repositories and report the findings, you must allow access to the following domains if:

  You’re running Checkov within your pipeline, enable access for the machine running Checkov.

  If you’re running the IDE extension on your local machine, enable access on the local machine.

| **Prisma Cloud URL is on** | **API Gateway**        | **S3 bucket for uploading findings**                                                                                                                                                                                              | **S3 bucket for routing to the correct S3 bucket**              |
| -------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| app3                       | api3.prismacloud.io    | <p>bc-scanner-results-890234264427-prod.s3.us-west-2.amazonaws.com<br>bc-scanner-results-890234264427-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-890234264427-prod.s3.us-west-2.amazonaws.com</p>           | bc-scanner-results-890234264427-prod.s3.us-west-2.amazonaws.com |
| app0                       | api0.prismacloud.io    | <p>bc-scanner-results-469330042197-prod.s3.us-east-1.amazonaws.com<br>bc-scanner-results-469330042197-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-469330042197-prod.s3.us-east-1.amazonaws.com</p>           | bc-scanner-results-469330042197-prod.s3.us-west-2.amazonaws.com |
| app                        | api.prismacloud.io     | <p>bc-scanner-results-838878234734-prod.s3.us-east-1.amazonaws.com<br>bc-scanner-results-838878234734-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-838878234734-prod.s3.us-east-1.amazonaws.com</p>           | bc-scanner-results-838878234734-prod.s3.us-west-2.amazonaws.com |
| app2                       | api2.prismacloud.io    | <p>bc-scanner-results-612480224350-prod.s3.us-east-2.amazonaws.com<br>bc-scanner-results-612480224350-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-612480224350-prod.s3.us-east-2.amazonaws.com</p>           | bc-scanner-results-612480224350-prod.s3.us-west-2.amazonaws.com |
| app4                       | api4.prismacloud.io    | <p>bc-scanner-results-540411623009-prod.s3.us-west-1.amazonaws.com<br>bc-scanner-results-540411623009-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-540411623009-prod.s3.us-west-1.amazonaws.com</p>           | bc-scanner-results-540411623009-prod.s3.us-west-2.amazonaws.com |
| app.ca                     | api.ca.prismacloud.io  | <p>bc-scanner-results-205367576728-prod.s3.ca-central-1.amazonaws.com<br>bc-scanner-results-205367576728-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-205367576728-prod.s3.ca-central-1.amazonaws.com</p>     | bc-scanner-results-205367576728-prod.s3.us-west-2.amazonaws.com |
| app.eu                     | api.eu.prismacloud.io  | <p>bc-scanner-results-836922451682-prod.s3.eu-central-1.amazonaws.com<br>bc-scanner-results-836922451682-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-836922451682-prod.s3.eu-central-1.amazonaws.com</p>     | bc-scanner-results-836922451682-prod.s3.us-west-2.amazonaws.com |
| app2.eu                    | api2.eu.prismacloud.io | <p>bc-scanner-results-800009193461-prod.s3.eu-west-1.amazonaws.com<br>bc-scanner-results-800009193461-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-800009193461-prod.s3.eu-west-1.amazonaws.com</p>           | bc-scanner-results-800009193461-prod.s3.us-west-2.amazonaws.com |
| app.ind                    | api.ind.prismacloud.io | <p>bc-scanner-results-018169107740-prod.s3.ap-south-1.amazonaws.com<br>bc-scanner-results-018169107740-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-018169107740-prod.s3.ap-south-1.amazonaws.com</p>         | bc-scanner-results-018169107740-prod.s3.us-west-2.amazonaws.com |
| app.id                     | api.id.prismacloud.io  | <p>bc-scanner-results-457807942906-prod.s3.ap-southeast-3.amazonaws.com<br>bc-scanner-results-457807942906-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-457807942906-prod.s3.ap-southeast-3.amazonaws.com</p> | bc-scanner-results-457807942906-prod.s3.us-west-2.amazonaws.com |
| app.fr                     | api.fr.prismacloud.io  | <p>bc-scanner-results-063178804405-prod.s3.eu-west-3.amazonaws.com<br>bc-scanner-results-063178804405-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-063178804405-prod.s3.eu-west-3.amazonaws.com</p>           | bc-scanner-results-063178804405-prod.s3.us-west-2.amazonaws.com |
| app-uk                     | api.uk.prismacloud.io  | <p>bc-scanner-results-580360239683-prod.s3.eu-west-2.amazonaws.com<br>bc-scanner-results-580360239683-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-580360239683-prod.s3.eu-west-2.amazonaws.com</p>           | bc-scanner-results-580360239683-prod.s3.us-west-2.amazonaws.com |
| app.jp                     | api.jp.prismacloud.io  | <p>bc-scanner-results-510882576293-prod.s3.ap-northeast-1.amazonaws.com<br>bc-scanner-results-510882576293-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-510882576293-prod.s3.ap-northeast-1.amazonaws.com</p> | bc-scanner-results-510882576293-prod.s3.us-west-2.amazonaws.com |
| app.sg                     | api.sg.prismacloud.io  | <p>bc-scanner-results-277833049433-prod.s3.ap-southeast-1.amazonaws.com<br>bc-scanner-results-277833049433-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-277833049433-prod.s3.ap-southeast-1.amazonaws.com</p> | bc-scanner-results-277833049433-prod.s3.us-west-2.amazonaws.com |
| app.anz                    | api.anz.prismacloud.io | <p>bc-scanner-results-607751493482-prod.s3.ap-southeast-2.amazonaws.com<br>bc-scanner-results-607751493482-prod.s3-accelerate.amazonaws.com<br>bc-vulnerabilities-utilities-607751493482-prod.s3.ap-southeast-2.amazonaws.com</p> | bc-scanner-results-607751493482-prod.s3.us-west-2.amazonaws.com |

* Adoption Advisor \*.ingest.sentry.io
* Launch Darkly

  \*.launchdarkly.com, to enable preview access to features. Also refer to the [public IP address list](https://docs.launchdarkly.com/home/advanced/public-ip-list#accessing-launchdarkly-through-a-public-ip-range) for Launch Darkly.
* Pendo

  Prisma Cloud uses Pendo for in-app analytics.

  * app.pendo.io
  * data.pendo.io
  * cdn.pendo.io
  * us.pendo.io, \*.us.pendo.io
  * \*.storage.googleapis.com
* Feature request submissions
  * prismacloud.ideas.aha.io cdn.aha.io
  * secure.gravatar.com
  * s3.amazonaws.com
* Images and fonts
  * use.typekit.net
  * p.typekit.net
  * fonts.googleapis.com
  * \*.storage.googleapis.com
  * fonts.gstatic.com
  * mt.google.com
* Palo Alto Support Portal and LiveCommunity
  * static.cloud.coveo.com
  * platform.cloud.coveo.com
  * nebula-cdn.kampyle.com
  * maxcdn.bootstrapcdn.com
  * use.fontawesome.com
  * ajax.googleapis.com
  * prod.hosted.lithcloud.com
  * static.hotjar.com
  * vars.hotjar.com
  * assets.adobedtm.com
  * paloaltonetworks.hosted.panopto.com
  * cdn.embed.ly
  * tag.demandbase.com
  * paloaltonetworks.d1.sc.omtrdc.net
  * cloudfront.net
  * cdn.pendo.io
  * data.pendo.io
  * firestore.googleapis.com
  * use.typekit.net
  * p.typekit.net
  * \*.youtube.com


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/get-started/console-prerequisites.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
