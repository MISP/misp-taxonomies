# MISP Taxonomies

[![Build Status](https://travis-ci.org/MISP/misp-taxonomies.svg?branch=master)](https://travis-ci.org/MISP/misp-taxonomies)

Taxonomies that can be used in [MISP](https://github.com/MISP/MISP) (2.4) and other information sharing tool and expressed in Machine Tags (Triple Tags). A machine tag is composed of a namespace (MUST), a predicate (MUST) and an (OPTIONAL) value. Machine tags are often called triple tag due to their format.

![Overview of the MISP taxonomies](tools/docs/images/taxonomy-explanation.png)

The following taxonomies can be used in MISP (as local or distributed tags) or in other tools willing to share common taxonomies among security information sharing tools.

The following taxonomies are described:

- [Admiralty Scale](./admiralty-scale)
- [adversary](./adversary) - description of an adversary infrastructure
- CIRCL [Taxonomy - Schemes of Classification in Incident Response and Detection](./circl)
- DE German (DE) [Government classification markings (VS)](./de-vs)
- [DHS CIIP Sectors](./dhs-ciip-sectors)
- [eCSIRT](./ecsirt) and IntelMQ incident classification
- [EU critical sectors](./eu-critical-sectors) - EU critical sectors
- [EUCI](./euci) - EU classified information marking
- [FIRST CSIRT Case](./first_csirt_case_classification) classification
- [Information Security Marking Metadata](./dni-ism) from DNI (Director of National Intelligence - US)
- [Malware](./malware) classification based on a SANS document
- [NATO Classification Marking](./nato)
- [OSINT Open Source Intelligence - Classification](./osint)
- [TLP - Traffic Light Protocol](./tlp)
- Vocabulary for Event Recording and Incident Sharing [VERIS](./veris)

### [Admiralty Scale](./admiralty-scale)

The Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information.

### [Adversary](./adversary)

An overview and description of the adversary infrastructure.

### CIRCL [Taxonomy - Schemes of Classification in Incident Response and Detection](./circl)

CIRCL Taxonomy is a simple scheme for incident classification and area topic where the incident took place.

### DE German (DE) [Government classification markings (VS)](./de-vs)

Taxonomy for the handling of protectively marked information in MISP with German (DE) Government classification markings (VS).

### [DHS CIIP Sectors](./dhs-ciip-sectors)

DHS critical sectors as described in https://www.dhs.gov/critical-infrastructure-sectors.

### [eCSIRT](./ecsirt) and IntelMQ incident classification

eCSIRT incident classification Appendix C of the eCSIRT EU project including IntelMQ updates.

### [EU Critical Sectors](./eu-critical-sectors)

Market operators and public administrations that must comply to some notifications requirements under EU NIS directive.

### [EUCI](./euci) classification

EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States [as described](http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013D0488&from=EN).

### [FIRST CSIRT Case](./first_csirt_case_classification) classification

FIRST CSIRT Case Classification.

### [Information Security Marking Metadata](./dni-ism) DNI (Director of National Intelligence - US)

ISM (Information Security Marking Metadata) [V13](http://www.dni.gov/index.php/about/organization/chief-information-officer/information-security-marking-metadata) as described by DNI.gov.

### [Malware](./malware) classification

Malware classification based on a [SANS whitepaper about malware](https://www.sans.org/reading-room/whitepapers/incident/malware-101-viruses-32848).

### [NATO Classification Marking](./nato)

Marking of Classified and Unclassified materials as described by the North Atlantic Treaty Organization, NATO.

### [TLP - Traffic Light Protocol](./tlp)

The Traffic Light Protocol - or short: TLP - was designed with the objective to create a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time.

### Vocabulary for Event Recording and Incident Sharing [VERIS](./veris)

Vocabulary for Event Recording and Incident Sharing is a format created by the [VERIS community](http://veriscommunity.net/).

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

