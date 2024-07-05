## About the connector
The WCF Restful Service - Push SMS supports single and bulk messages request with parameterized or customized message.
<p>This document provides information about the Ducont SMS Connector, which facilitates automated interactions, with a Ducont SMS server using FortiSOAR&trade; playbooks. Add the Ducont SMS Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Ducont SMS.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-ducont-sms`

## Prerequisites to configuring the connector
- You must have the URL of Ducont SMS server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Ducont SMS server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Ducont SMS</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Ducont SMS server to connect and perform automated operations.<br>
<tr><td>User Id<br></td><td>Specify the user id of the Ducont SMS server to connect and perform automated operations.<br>
<tr><td>Password<br></td><td>Specify the password of the Ducont SMS server to connect and perform automated operations.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Push SMS<br></td><td><br></td><td>push_sms <br/>Utility<br></td></tr>
<tr><td>Push SMS SUB<br></td><td><br></td><td>push_sms_sub <br/>Utility<br></td></tr>
</tbody></table>

### operation: Push SMS
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Channel Id<br></td><td>Specify the channel id of the Ducont SMS server.<br>
</td></tr><tr><td>Sender Id<br></td><td>Specify the sender id of the Ducont SMS.<br>
</td></tr><tr><td>Message Id<br></td><td>Specify the message ID of the Ducont SMS.<br>
</td></tr><tr><td>Priority<br></td><td>Priority of the message.<br>
</td></tr><tr><td>Recipients<br></td><td>Specify comma separated recipients in case of multiple .<br>
</td></tr><tr><td>Template Id<br></td><td>Specify the template ID of the Ducont SMS.<br>
</td></tr><tr><td>Template Variables<br></td><td>Specify the template variables of the Ducont SMS.<br>
</td></tr><tr><td>Validity Period<br></td><td>Specify the validity period of the Ducont SMS.<br>
</td></tr><tr><td>Language Id<br></td><td>Specify the language ID of the Ducont SMS.<br>
</td></tr><tr><td>Confirm Delivery<br></td><td>This flag (true or false) will be used if Call backURL is required<br>
<strong>If you choose 'true'</strong><ul><li>Status Callback URL: </li></ul><strong>If you choose 'false'</strong><ul><li>Status Callback URL: </li></ul></td></tr><tr><td>Body<br></td><td>Specify the message body of the Ducont SMS.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "01",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Message": "Message sent successfully."
</code><code><br>}</code>

### operation: Push SMS SUB
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Channel Id<br></td><td>Specify the channel id of the Ducont SMS server.<br>
</td></tr><tr><td>Sender Id<br></td><td>Specify the sender id of the Ducont SMS.<br>
</td></tr><tr><td>Message Id<br></td><td>Specify the message ID of the Ducont SMS.<br>
</td></tr><tr><td>Priority<br></td><td>Priority of the message.<br>
</td></tr><tr><td>Recipients<br></td><td>Specify comma separated recipients in case of multiple .<br>
</td></tr><tr><td>Template Id<br></td><td>Specify the template ID of the Ducont SMS.<br>
</td></tr><tr><td>Template Variables<br></td><td>Specify the template variables of the Ducont SMS.<br>
</td></tr><tr><td>Validity Period<br></td><td>Specify the validity period of the Ducont SMS.<br>
</td></tr><tr><td>Language Id<br></td><td>Specify the language ID of the Ducont SMS.<br>
</td></tr><tr><td>Confirm Delivery<br></td><td>This flag (true or false) will be used if Call backURL is required<br>
<strong>If you choose 'true'</strong><ul><li>Status Callback URL: </li></ul><strong>If you choose 'false'</strong><ul><li>Status Callback URL: </li></ul></td></tr><tr><td>Body<br></td><td>Specify the message body of the Ducont SMS.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Status": "01",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Message": "Message sent successfully."
</code><code><br>}</code>
## Included playbooks
The `Sample - ducont-sms - 1.0.0` playbook collection comes bundled with the Ducont SMS connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Ducont SMS connector.

- Push SMS
- Push SMS SUB

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
