# MISP Taxonomies

Taxonomies that can be used in [MISP](https://github.com/MISP/MISP) (2.4) and other information sharing tool and expressed in Machine Tags (Triple Tags). A machine tag is composed of a namespace (MUST), a predicate (MUST) and an (OPTIONAL) value. Machine tags are often called triple tag due to their format.

![Overview of the MISP taxonomies](tools/docs/images/taxonomy-explanation.png)

The following taxonomies can be used in MISP (as local or distributed tags) or in other tools willing to share common taxonomies among security information sharing tools.

The following taxonomies are described:

- [Admiralty Scale](./admiralty-scale)
- CIRCL [Taxonomy - Schemes of Classification in Incident Response and Detection](./circl)
- [eCSIRT](./ecsirt) and IntelMQ incident classification
- [EUCI](./euci) - EU classified information marking
- [FIRST CSIRT Case Classification](./first_csirt_case_classification) - FIRST CSIRT Case Classification
- [Information Security Marking Metadata](./dni-ism) from DNI (Director of National Intelligence - US)
- [NATO Classification Marking](./nato)
- [OSINT Open Source Intelligence - Classification](./osint)
- [TLP - Traffic Light Protocol](./tlp)
- Vocabulary for Event Recording and Incident Sharing [VERIS](./veris)

### [Admiralty Scale](./admiralty-scale)

The Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information.

### CIRCL [Taxonomy - Schemes of Classification in Incident Response and Detection](./circl)

CIRCL Taxonomy is a simple scheme for incident classification and area topic where the incident took place.

### [eCSIRT](./ecsirt) and IntelMQ incident classification

eCSIRT incident classification Appendix C of the eCSIRT EU project including IntelMQ updates.

### [EUCI](./euci) classification

EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States [as described](http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013D0488&from=EN).

### [FIRST CSIRT Case Classification](./first_csirt_case_classification) - FIRST CSIRT Case Classification

FIRST CSIRT Case Classification according to [FIRST.org](https://www.first.org/_assets/resources/guides/csirt_case_classification.html)

### [Information Security Marking Metadata](./dni-ism) DNI (Director of National Intelligence - US)

ISM (Information Security Marking Metadata) [V13](http://www.dni.gov/index.php/about/organization/chief-information-officer/information-security-marking-metadata) as described by DNI.gov.

### [NATO Classification Marking](./nato)

Marking of Classified and Unclassified materials as described by the North Atlantic Treaty Organization, NATO.

### [TLP - Traffic Light Protocol](./tlp)

The Traffic Light Protocol - or short: TLP - was designed with the objective to create a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time.

### Vocabulary for Event Recording and Incident Sharing [VERIS](./veris)

Vocabulary for Event Recording and Incident Sharing is a format created by the [VERIS community](http://veriscommunity.net/).

# How to contribute your taxonomy?

It is quite easy. Create a JSON file describing your taxonomy as triple tags (e.g. check an existing one like [Admiralty Scale](./admiralty-scale)), create a directory matching your name space, put your machinetag file in the directory and pull your request. That's it. Everyone can benefit from your taxonomy and can be automatically enabled in information sharing tools like MISP.

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

