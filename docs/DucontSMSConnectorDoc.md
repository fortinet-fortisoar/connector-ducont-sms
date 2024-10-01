## About the connector
The WCF Restful Service - Push SMS supports single and bulk messages request with parameterized or customized message.
<p>This document provides information about the Ducont SMS Connector, which facilitates automated interactions, with a Ducont SMS server using FortiSOAR&trade; playbooks. Add the Ducont SMS Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Ducont SMS.</p>

### Version information

Connector Version: 1.0.0

Authored By: spryIQ.co

Contributors: Jitesh Rathod

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-ducont-sms</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Ducont SMS server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Ducont SMS server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Ducont SMS</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Ducont SMS server to connect and perform automated operations.</td>
</tr><tr><td>User Id</td><td>Specify the user id of the Ducont SMS server to connect and perform automated operations.</td>
</tr><tr><td>Password</td><td>Specify the password of the Ducont SMS server to connect and perform automated operations.</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Push SMS</td><td>Send a message to one or more recipients through the Ducont SMS service using the specified input parameters.</td><td>push_sms <br/>Investigation</td></tr>
<tr><td>Push SMS SUB</td><td>Send subscription-based SMS messages through the Ducont SMS service.</td><td>push_sms_sub <br/>Investigation</td></tr>
</tbody></table>

### operation: Push SMS
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Recipient Mobile Numbers</td><td>Specify the CSV list of mobile number of the user to whom you want to send the message.
</td></tr><tr><td>Body</td><td>Specifies the content of the SMS message being sent.
</td></tr><tr><td>Sender ID</td><td>Specify a custom identifier that will be displayed as the sender of the SMS message.
</td></tr><tr><td>Message ID</td><td>Specify a unique identifier assigned to each SMS message sent through the Ducont SMS service.
</td></tr><tr><td>Priority</td><td>Select the priority level of the SMS message being sent through the Ducont SMS service
</td></tr><tr><td>Channel ID</td><td>Specify a communication channel through which the SMS message is sent.
</td></tr><tr><td>Template ID</td><td>Specify a predefined message template for the SMS being sent through the Ducont SMS service.
</td></tr><tr><td>Template Variables</td><td>Specify the template variables of the Ducont SMS.
</td></tr><tr><td>Validity Period</td><td>Specifies the duration for which the SMS message remains valid for delivery after it has been sent. Default is 7200
</td></tr><tr><td>Language ID</td><td>Specifies the language in which the SMS message should be sent. Default is EN.
</td></tr><tr><td>Confirm Delivery</td><td>Specifies whether the sender wishes to receive a confirmation of the message's delivery status.
<br><strong>If you choose 'true'</strong><ul><li>Status Callback URL: Specify a URL endpoint where the SMS service can send a notifications regarding the delivery status of sent messages.</li></ul><strong>If you choose 'false'</strong><ul><li>Status Callback URL: Specify a URL endpoint where the SMS service can send a notifications regarding the delivery status of sent messages.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "Status": "",
        "Message": ""
    }
]</pre>
### operation: Push SMS SUB
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Recipient Mobile Numbers</td><td>Specify the CSV list of mobile number of the user to whom you want to send the message.
</td></tr><tr><td>Body</td><td>Specifies the content of the SMS message being sent.
</td></tr><tr><td>Channel ID</td><td>Specify a communication channel through which the SMS message is sent.
</td></tr><tr><td>Sender ID</td><td>Specify a custom identifier that will be displayed as the sender of the SMS message.
</td></tr><tr><td>Message ID</td><td>Specify a unique identifier assigned to each SMS message sent through the Ducont SMS service.
</td></tr><tr><td>Priority</td><td>Select the priority level of the SMS message being sent through the Ducont SMS service
</td></tr><tr><td>Template ID</td><td>Specify a predefined message template for the SMS being sent through the Ducont SMS service.
</td></tr><tr><td>Template Variables</td><td>Specify the template variables of the Ducont SMS.
</td></tr><tr><td>Validity Period</td><td>Specifies the duration for which the SMS message remains valid for delivery after it has been sent. Default is 7200
</td></tr><tr><td>Language ID</td><td>Specifies the language in which the SMS message should be sent. Default is EN.
</td></tr><tr><td>Confirm Delivery</td><td>Specifies whether the sender wishes to receive a confirmation of the message's delivery status.
<br><strong>If you choose 'true'</strong><ul><li>Status Callback URL: Specify a URL endpoint where the SMS service can send a notifications regarding the delivery status of sent messages.</li></ul><strong>If you choose 'false'</strong><ul><li>Status Callback URL: Specify a URL endpoint where the SMS service can send a notifications regarding the delivery status of sent messages.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "Status": "",
        "Message": ""
    }
]</pre>
