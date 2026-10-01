---
title: RSyslog Integration with AccuKnox
description: The RSyslog integration with AccuKnox enables forwarding logs and alerts to a centralized RSyslog server. This integration ensures that all logs and alerts are securely stored and managed in a centralized location, enhancing visibility and security monitoring capabilities.
---

![rsyslog-accuknox](./images/rsyslog-accuknox.png)

## **Overview**

RSYSLOG is the <b>r</b>ocket-fast <b>sys</b>tem for <b>log</b> processing.
It offers high-performance, great security features and a modular design. While it started as a regular syslogd, rsyslog has evolved into a kind of swiss army knife of logging, being able to accept inputs from a wide variety of sources, transform them, and output to the results to diverse destinations.
In the case of a deployment with a high rate of log generation, or to store on a server to forward it to other sources like Datadog, McAfee SIEM, Azure Sentinel, AlienVault, etc., you can forward syslogs over an Ethernet interface to prevent loss of logs and reduce the load on the management interface, which optimizes management operations.

## Prerequisites

- A running RSyslog server.
- Host name/IP, Port number, Transport type(TCP or UDP)
- Feeder Service Running on Client's cluster.

  **_Note_** : To deploy RSyslog server , [RSyslog Documentation ](https://www.rsyslog.com/doc/v8-stable/).

## Configuration

To forward the Alerts based on Policy Violation to RSyslog Server set the following environment variables `RSYSLOG_FEEDER_ENABLED` and `RSYSLOG_ALERTS_ENABLED` to `true` and to forward Logs `RSYSLOG_LOGS_ENABLED` to `true` in your Feeder Agent manifest.

Also set the environment variables `RSYSLOG_URL`, `RSYSLOG_TRANSPORT`, `RSYSLOG_PORT` of the RSyslog Server Deployed.
To start editing the chart:

```sh
kubectl edit deployment feeder-service -n accuknox-agents
```

Edit the following Enviornment Variables mentioned below:

```yaml
- name: RSYSLOG_FEEDER_ENABLED
  value: "true"
- name: RSYSLOG_ALERTS_ENABLED
  value: "true"
- name: RSYSLOG_LOGS_ENABLED
  value: "true"
- name: RSYSLOG_URL
  value: 34.XX.XX.XXX
- name: RSYSLOG_PORT
  value: 514
- name: RSYSLOG_TRANSPORT
  value: tcp
```

**OR** </br>
To set the the envionment variables on Run Time to Integrate the Rsyslog with Feeder Service Agent, One can use a single command.

```sh
kubectl set env deploy/feeder-service -n accuknox-agents RSYSLOG_ALERTS_ENABLED=true RSYSLOG_FEEDER_ENABLED=true RSYSLOG_LOGS_ENABLED=false RSYSLOG_URL=<RSYSLOG_IP> RSYSLOG_PORT=<RSYSLOG_PORT> RSYSLOG_TRANSPORT=<RSYSLOG_TRANSPORT>
```

Replace `<RSYSLOG_IP>` , `<RSYSLOG_PORT>` and `<RSYSLOG_TRANSPORT>` from your Rsyslog Server.

## Environment variables for RSyslog Integration

The following is the list of environment variables available for the Feeder-Service-Agent

| Env Variable                    | Description                                                                                                                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| `RSYSLOG_FEEDER_ENABLED`        | Setting this to `true` forward the Logs and Alerts to RSyslog Server                                                                                                                                                       |
| `RSYSLOG_ALERTS_ENABLED`        | Setting this to `true` forward the Policy Violated Alerts to RSyslog Server                                                                                                                                                |
| `RSYSLOG_LOGS_ENABLED`          | Setting this to `true` forward the Logs to RSyslog Server                                                                                                                                                                  |
| `RSYSLOG_URL`                   | Enter your RSyslog Server address here, IP address or fully qualified domain name (FQDN) of the RSyslog server. For example: `rsyslog.mydomain.com` or `35.xx.xx.xx`                                                       |     |
| `RSYSLOG_PORT`                  | The port number to use when sending syslog messages (default is UDP on port 514); you must use the same port number. e.g., `514`                                                                                           |
| `RSYSLOG_TRANSPORT`             | Add `udp`,`tcp` or `tcp+tls`as the method of communication with the RSyslog server. <br>**\*Note\*\***: _The methods here are case sensitive, add as mentioned and to enable tls users need to pass the path to .pem file_ |
| `RSYSLOG_TLS_CERTIFICATES_PATH` | Add the `path/to/certificate.pem` , <br>**\*Note\*\***: Create the secret manually and mount it on feeder service by specifying the mounts in feederService.volumeMounts[] and feederService.volumes[]                     |

Once the enviornment variables are passed and deployment is updated, the feeder service pod restarts and Logs and Alerts are forwarded to Integrated RSyslog Server from Feeder Service.
To view the same check the `/var/log` folder inside the RSyslog Server. A directory with name `feeder-service` is created and all the logs are stored inside the same directory as a log file.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
