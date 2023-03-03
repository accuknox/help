---
hide:
  - toc
---

## RSyslog Integration

To forward the events to RSyslog you must first set up the RSyslog Integration.

### Integration of RSyslog:
#### **a. Prerequisites:**
+ A running RSyslog server.
+ Host name/IP, Port number, Transport type(TCP or UDP)

**Note:** To deploy RSyslog server , [RSyslog Documentation] (https://www.rsyslog.com/doc/v8-stable/) .

#### **b. Steps to Integrate:**

+ Go to Settings → Integrations → CWPP(Tab).
+ Click integrate now on RSyslog.
+ Fill up the following fields:
    + **Integration Name:** Enter the name for the integration. You can set any name of your choice. e.g., ```sh Container Security Alerts ```

    + **Server Address:** Enter your RSyslog Server address here, IP address or fully qualified domain name (FQDN) of the RSyslog server e.g.,```sh rsyslog.mydomain.com or 35.xx.xx.xx ```

    + **Port:** The port number to use when sending RSyslog messages (default is UDP on port 514); you must use the same port number. e.g., ```sh 514 ```

    + **Transport:** Select UDP, or TCP as the method of communication with the RSyslog server

+ Click **Test** to check the new functionality, You will receive the test message on configured RSyslog Server. ```sh -Test message Please ignore !!```

+ Click **Save** to save the Integration. You can now configure Alert Triggers for RSyslog Events