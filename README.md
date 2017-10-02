# MISP Taxonomies

[![Build Status](https://travis-ci.org/MISP/misp-taxonomies.svg?branch=master)](https://travis-ci.org/MISP/misp-taxonomies)

Taxonomies that can be used in [MISP](https://github.com/MISP/MISP) (2.4) and other information sharing tool and expressed in Machine Tags (Triple Tags). A machine tag is composed of a namespace (MUST), a predicate (MUST) and an (OPTIONAL) value. Machine tags are often called triple tag due to their format.

![Overview of the MISP taxonomies](tools/docs/images/taxonomy-explanation.png)

The following taxonomies can be used in MISP (as local or distributed tags) or in other tools willing to share common taxonomies among security information sharing tools.

The following taxonomies are described:

- [Admiralty Scale](./admiralty-scale)
- [adversary](./adversary) - description of an adversary infrastructure
- CIRCL [Taxonomy - Schemes of Classification in Incident Response and Detection](./circl)
- [The CSSA agreed sharing taxonomy](./cssa)
- [Collaborative intelligence](./collaborative-intelligence) - Collaborative intelligence support language is a common language to support analysts to perform their analysis to get crowdsourced support when using threat intelligence sharing platform like MISP. The objective of this language is to advance collaborative analysis and to share earlier than later.
- [Cyber Kill Chain](./kill-chain) from Lockheed Martin
- DE German (DE) [Government classification markings (VS)](./de-vs)
- [DHS CIIP Sectors](./dhs-ciip-sectors)
- [Diamond Model for Intrusion Analysis](./diamond-model)
- [Detection Maturity Level](./DML)
- [Domain Name Abuse](./domain-abuse)
- [eCSIRT](./ecsirt) and IntelMQ incident classification
- [ENISA](./enisa) ENISA Threat Taxonomy
- [Estimative Language](./estimative-language) Estimative Language (ICD 203)
- [EU NIS Critical Infrastructure Operators](./eu-marketop-and-publicadmin) - EU NIS Critical Infrastructure Operators
- [EUCI](./euci) - EU classified information marking
- [Europol Incident](./europol-incident) - Europol class of incident taxonomy
- [Europol Events](./europol-event) - Europol type of events taxonomy
- [FIRST CSIRT Case](./csirt_case_classification) classification
- [FIRST Information Exchange Policy (IEP)](./iep) framework
- [Information Security Indicators](./information-security-indicators) -  ETSI GS ISI 001-1 (V1.1.2): ISI Indicators
- [Information Security Marking Metadata](./dni-ism) from DNI (Director of National Intelligence - US)
- [Malware](./malware_classification) classification based on a SANS document
- [ms-caro-malware](./ms-caro-malware) Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology.
- [NATO Classification Marking](./nato)
- [Open Threat Taxonomy v1.1 (SANS)](./open_threat)
- [OSINT Open Source Intelligence - Classification](./osint)
- [STIX-TTP](./stix-ttp) - Represents the behavior or modus operandi of cyber adversaries as normalized in STIX
- [Stealth Malware Taxonomy as defined by Joanna Rutkowska](./stealth-malware)
- [The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used.](./PAP)
- [Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer.](./targeted-threat-index)
- [TLP - Traffic Light Protocol](./tlp)
- [Vocabulaire des probabilités estimatives](./vocabulaire-des-probabilites-estimatives)
- Vocabulary for Event Recording and Incident Sharing [VERIS](./veris)
- [Binary Classification](./binary-class) safe/malicious binary tagging

### [Admiralty Scale](./admiralty-scale)

The Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information.

### [Adversary](./adversary)

An overview and description of the adversary infrastructure.

### CIRCL [Taxonomy - Schemes of Classification in Incident Response and Detection](./circl)

CIRCL Taxonomy is a simple scheme for incident classification and area topic where the incident took place.

### [Cyber Kill Chain](./kill-chain) from Lockheed Martin

Cyber Kill Chain from Lockheed Martin as described in [Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf).

### DE German (DE) [Government classification markings (VS)](./de-vs)

Taxonomy for the handling of protectively marked information in MISP with German (DE) Government classification markings (VS).

### [DHS CIIP Sectors](./dhs-ciip-sectors)

DHS critical sectors as described in https://www.dhs.gov/critical-infrastructure-sectors.

### [Diamond Model for Intrusion Analysis](./diamond-model)

The Diamond Model for Intrusion Analysis, a phase-based model developed by Lockheed Martin, aims to help categorise and identify the stage of an attack
as described in [http://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf](http://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf).

### [Detection Maturity Level](./DML)

The Detection Maturity Level (DML) model is a capability maturity model for referencing ones maturity in detecting cyber attacks.  It's designed for organizations who perform intel-driven detection and response and who put an emphasis on having a mature detection program.

### [Domain Name Abuse](./domain-abuse)

Taxonomy to tag domain names used for cybercrime.
We suggest to use europol-incident(./europol-incident) to tag abuse-activity.

### [eCSIRT](./ecsirt) and IntelMQ incident classification

eCSIRT incident classification Appendix C of the eCSIRT EU project including IntelMQ updates.

### [ENISA](./enisa) ENISA Threat Taxonomy

ENISA Threat Taxonomy - A tool for structuring threat information [as published](https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends/enisa-threat-landscape/etl2015/enisa-threat-taxonomy-a-tool-for-structuring-threat-information)

### [Estimative Language](./estimative-language) Estimative Language (ICD 203)

Estimative language - including likelihood or probability of event based on the Intelligence Community Directive 203 (ICD 203) (6.2.(a)).

### [EU NIS Critical Infrastructure Operators](./eu-marketop-and-publicadmin)

Market operators and public administrations that must comply to some notifications requirements under EU NIS directive.

### [EUCI](./euci) classification

EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States [as described](http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013D0488&from=EN).

### [Europol Incident](./europol-incident)

EUROPOL class of incident taxonomy

### [Europol Events](./europol-event)

EUROPOL type of events taxonomy

### [FIRST CSIRT Case](./csirt_case_classification) classification

FIRST CSIRT Case Classification.

### [FIRST Information Exchange Policy (IEP)](./iep) framework

### [Information Security Indicators](./information-security-indicators) -  ETSI GS ISI 001-1 (V1.1.2): ISI Indicators

Information security indicators have been standardized by the [ETSI Industrial Specification Group (ISG) ISI](http://www.etsi.org/technologies-clusters/technologies/information-security-indicators). These indicators provide the basis to switch from a qualitative to a quantitative culture in IT Security Scope of measurements: External and internal threats (attempt and success), user's deviant behaviours, nonconformities and/or vulnerabilities (software, configuration, behavioural, general security framework).

### [Information Security Marking Metadata](./dni-ism) DNI (Director of National Intelligence - US)

ISM (Information Security Marking Metadata) [V13](http://www.dni.gov/index.php/about/organization/chief-information-officer/information-security-marking-metadata) as described by DNI.gov.

### [Malware](./malware_classification) classification

Malware classification based on a [SANS whitepaper about malware](https://www.sans.org/reading-room/whitepapers/incident/malware-101-viruses-32848).

### [ms-caro-malware](./ms-caro-malware) Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology.

### [NATO Classification Marking](./nato)

Marking of Classified and Unclassified materials as described by the North Atlantic Treaty Organization, NATO.

### [Open Threat Taxonomy v1.1](./open_threat)

Open Threat Taxonomy v1.1 base on James Tarala of SANS [ref](http://www.auditscripts.com/resources/open_threat_taxonomy_v1.1a.pdf).

### [STIX-TTP](./stix-ttp)

STIX-TTP exposes a set classification tools that represents the behavior or modus operandi of cyber adversaries as normalized in STIX. TTPs consist of the specific adversary behavior (attack patterns, malware, exploits) exhibited, resources leveraged (tools, infrastructure, personas), information on the victims targeted (who, what or where), relevant ExploitTargets being targeted, intended effects, relevant kill chain phases, handling guidance, source of the TTP information, etc.

### [Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer.](./targeted-threat-index)

The Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer. The TTI metric was first introduced at SecTor 2013 by Seth Hardy as part of the talk “RATastrophe: Monitoring a Malware Menagerie” along with Katie Kleemola and Greg Wiseman. [More info about TTI](https://citizenlab.org/2013/10/targeted-threat-index/).

### [The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used.](./PAP)

The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used. It's a protocol/taxonomy similar to TLP informing the recipients of information what they can do with the received information.

### [TLP - Traffic Light Protocol](./tlp)

The Traffic Light Protocol - or short: TLP - was designed with the objective to create a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time.

### Vocabulary for Event Recording and Incident Sharing [VERIS](./veris)

Vocabulary for Event Recording and Incident Sharing is a format created by the [VERIS community](http://veriscommunity.net/).

# Reserved Taxonomy

The following taxonomy namespaces are reserved and used internally to MISP.

- [galaxy](./galaxy/) mapping taxonomy with cluster:element:"value".

# Documentation

A documentation of the taxonomies is [generated automatically](https://github.com/MISP/misp-taxonomies/blob/master/tools/machinetag.py) from the taxonomies description and available in [PDF](https://www.misp.software/taxonomies.pdf) and [HTML](https://www.misp.software/taxonomies.html).

# How to contribute your taxonomy?

It is quite easy. Create a JSON file describing your taxonomy as triple tags (e.g. check an existing one like [Admiralty Scale](./admiralty-scale)), create a directory matching your name space, put your machinetag file in the directory and pull your request. That's it. Everyone can benefit from your taxonomy and can be automatically enabled in information sharing tools like [MISP](https://www.github.com/MISP/MISP).

For more information, "[Information Sharing and Taxonomies Practical Classification of Threat Indicators using MISP](https://www.circl.lu/assets/files/misp-training/3.2-MISP-Taxonomy-Tagging.pdf)" presentation given to the last MISP training in Luxembourg.

# How to add your private taxonomy to MISP

~~~~shell
$ cd /var/www/MISP/app/files/taxonomies/
$ mkdir privatetaxonomy
$ cd privatetaxonomy
$ vi machinetag.json
~~~~

Create a JSON file Create a JSON file describing your taxonomy as triple tags.

Once you are happy with your file go to MISP Web GUI taxonomies/index and update the taxonomies, the newly created taxonomy should be visible, now you need to activate the tags within your taxonomy.

# MISP Taxonomies - tools

[machinetag.py](./tools/machinetag.py) is a parsing tool to dump taxonomies expressed in Machine Tags (Triple Tags) and list all valid tags from a specific taxonomy.

~~~~shell
% cd tools
% python machinetag.py
        admiralty-scale:source-reliability="a"
        admiralty-scale:source-reliability="b"
        admiralty-scale:source-reliability="c"
        admiralty-scale:source-reliability="d"
        admiralty-scale:source-reliability="e"
        admiralty-scale:source-reliability="f"
        admiralty-scale:information-credibility="1"
        admiralty-scale:information-credibility="2"
        admiralty-scale:information-credibility="3"
        admiralty-scale:information-credibility="4"
        admiralty-scale:information-credibility="5"
        admiralty-scale:information-credibility="6"
        ...
~~~~

# License

The MISP taxonomies are licensed under [CC0 1.0 Universal (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/) -  Public Domain Dedication. If a specific author of a taxonomy wants to license it under a different license, a pull request can be requested.
