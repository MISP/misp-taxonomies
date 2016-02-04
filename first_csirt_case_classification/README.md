# FIRST CSIRT Case Classification

https://www.first.org/_assets/resources/guides/csirt_case_classification.html

## Incident Categories

All incidents managed by the CSIRT should be classified into one of the categories listed in the table below. 

<dl>
<dt>Denial of service</dt>
<dd>Sensitivity: S3<dd>
<dd>DOS or DDOS attack.</dd>

<dt>Forensics</dt>
<dd>Sensitivity: S1<dd>
<dd>Any forensic work to be done by CSIRT<dd>

<dt>Compromised Information</dt>
<dd>Sensitivity: S1<dd>
<dd>Attempted or successful destruction, corruption, or disclosure of sensitive corporate information or Intellectual Property.</dd>

<dt>Compromised Asset</dt>
<dd>Sensitivity: S1,S2<dd>
<dd>Compromised host (root account, Trojan, rootkit), network device, application, user account.  This includes malware-infected hosts where an attacker is actively controlling the host.</dd>

<dt>Unlawful activity</dt>
<dd>Sensitivity: S1<dd>
<dd>Theft / Fraud / Human Safety / Child Porn.  Computer-related incidents of a criminal nature, likely involving law enforcement, Global Investigations, or Loss Prevention.</dd>

<dt>Internal Hacking</dt>
<dd>Sensitivity: S1, S2, S3<dd>
<dd>Reconnaissance or Suspicious activity originating from inside the Company corporate network, excluding malware.</dd>

<dt>External Hacking</dt>
<dd>Sensitivity: S1, S2, S3<dd>
<dd>Reconnaissance or Suspicious Activity originating from outside the Company corporate network (partner network, Internet), excluding malware.</dd>

<dt>Malware</dt>
<dd>Sensitivity: S3<dd>
<dd>A virus or worm typically affecting multiple corporate devices.  This does not include compromised hosts that are being actively controlled by an attacker via a backdoor or Trojan. (See Compromised Asset)</dd>

<dt>Email</dt>
<dd>Sensitivity: S3<dd>
<dd>Spoofed email, SPAM, and other email security-related events.</dd>

<dt>Consulting</dt>
<dd>Sensitivity: S1, S2, S3<dd>
<dd>Security consulting unrelated to any confirmed incident.</dd>

<dt>Policy Violations</dt>
<dd>Sensitivity: S1, S2, S3<dd>
<dd>Sharing offensive material, sharing/possession of copyright material.<dd>
<dd>Deliberate violation of Infosec policy.<dd>
<dd>Inappropriate use of corporate asset such as computer, network, or application.<dd>
<dd>Unauthorized escalation of privileges or deliberate attempt to subvert access controls.</dd>


</dl>

## Criticality Classification

The criticality matrix defines the minimal customer response time and ongoing communication requirements for a case.  The criticality level should be entered into the ITS when a case is created, and it should not be altered at any point during the case lifecycle except when it was incorrectly classified in the first place.   Typically the IM will determine the criticality level.  In some cases it will be appropriate for the IM to work with the customer to determine the criticality level.

 

<dl>
<dt>1</dt>
<dd>Incident affecting critical systems or information with potential to be revenue or customer impacting.</dd>
<dt>2</dt>
<dd>Incident affecting non-critical systems or information, not revenue or customer impacting. Employee investigations that are time sensitive should typically be classified at this level.</dd>
<dt>3</dt>
<dd>Possible incident, non-critical systems.  Incident or employee investigations that are not time sensitive.  Long-term investigations involving extensive research and/or detailed forensic work.</dd>
</dl>

## Sensitivity Classification

CSIRT IM’s should always apply the “need to know” principle when communicating case details with other parties. The sensitivity matrix below helps to define “need to know” by classifying cases according to sensitivity level.  The ‘Required’ column defines the parties that “need to know” for a given sensitivity level.  The ‘Optional’ column defines the other parties that may be included on communications, if necessary.  Typically the IM will determine the sensitivity level.  In some cases it will be appropriate for the IM to work with the customer to determine the sensitivity level.

<dl>
<dt>1</dt>
<dd>Extremely Sensitive.</dd>
<dt>2</dt>
<dd>Sensitive.</dd>
<dt>3</dt>
<dd>Not Sensitive.</dd>
</dl>


# Machine-parsable FIRST CSIRT Case Classification

The repository contains a [JSON file including the machine-parsable tags](machinetag.json)
along with their human-readable description. The software can use both
representation on the user-interface and store the tag as machine-parsable.

~~~~
csirt_case_classification:incident-category="internal-hacking"
~~~~


Author:   Dustin Schieber dschiebe@cisco.com  Gavin Reid gavreid@cisco.com


