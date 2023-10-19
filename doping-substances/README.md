# MISP_DopingSubstanceTaxonomy

This project aims to gather information about all the prohibited sports Doping Substances. 

We collected all of the information on the [WADA website](https://www.wada-ama.org/en/prohibited-list).

To do that we have created a python script to scrap this website and generate a JSON file (Taxonomy).

This Taxonomy could be add in MISP to help sports organizations to fight against usage of doping substances.

## MISP

![logo](Misp-logo.png)

What is MISP ?

>A threat intelligence platform for sharing, storing and correlating 
Indicators of Compromise of targeted attacks, threat intelligence, 
financial fraud information, vulnerability information or even 
counter-terrorism information. Discover how MISP is used today in 
multiple organisations. Not only to store, share, collaborate on cyber 
security indicators, malware analysis, but also to use the IoCs and 
information to detect and prevent attacks, frauds or threats against ICT
 infrastructures, organisations or people.

## JSON Generation

In order to build the JSON file, we created a Python script which scrap the WADA (World Anti-Doping Agency) ‘s prohibited list.

Thanks to BeautifulSoup, a useful library that helps a lot when it comes to scrap HTLM documents, the script is able to get all the list of doping substances.

The file is created with PyTaxonomies, a MISP library that help to create valid JSON file according to the [MISP Platform](https://www.misp-project.org/taxonomies.html#_misp_taxonomies).

Finally, the script generates all predicates (doping categories) and the entries associated (the doping substances themselves).

## Installation

If you want to try it out yourself, you need to have both BeautifulSoup & PyTaxonomies installated.

## Authors

DELUS Thibaut : https://github.com/WooZyhh

JACOB Lucas : https://github.com/Chaamoxs
