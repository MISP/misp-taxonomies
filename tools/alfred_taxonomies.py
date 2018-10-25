#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import json
from pytaxonomies import Taxonomy, Predicate, Entry

'''
Taxonomies mapping:
    * disclosure-type, origin, originating-organization, exploitation-technique => part of cccs
    * dos-type ~~ ddos
    * report-state ~~ workflow
    * malware-category ~~ malware_classification - NOPE: malware_classification has a static source @ SANS

* access-method - ack
* approved-category-of-action - ack
* cccs - ack
* interception method -> ack

* domain-category & ip-category - maybe?
* email-type - malicious email types - maybe?
* maliciousness -> maybe?
* malware-category -> yes?
* scan type: maybe?

* severity: atta&ck?
* misusage-type -> attack?
* mitigation type -> attack?

* threat-vector: languages/applications/protocols -> split

* ftp-type - request / response => object
* record type: (query/response) => part of object

* host category -> server/workstation  -> part of object : network device

* method match -> HTTP request type ?!
'''

root_dir_taxonomies = Path('..')

ontology_path = Path('alfred-ontology.json')

with open(ontology_path) as f:
    ontology = json.load(f)['data']

# CCCS Taxonomy
cccs = Taxonomy()
cccs.name = "cccs"
cccs.description = "Internal taxonomy for CCCS."
cccs.version = 1
cccs.expanded = "CCCS"
cccs.predicates = {}

# Tags for internal reference
predicate = Predicate()
predicate.predicate = 'event'
predicate.expanded = 'Event type'
predicate.description = 'Type of event associated to the internal reference'
predicate.entries = {}

for datatype in ontology['dataTypes']:
    if 'superType' not in datatype or datatype['superType'] != 'EVENT':
        continue
    entry = Entry()
    entry.value = datatype['name'].lower().replace('_', '-')
    entry.expanded = datatype['name'].lower().replace('_', ' ').capitalize()
    entry.description = datatype['description'].replace(' The value is the event ID.', '')
    predicate.entries[entry.value] = entry

cccs.predicates[predicate.predicate] = predicate

predicate_of_cccs = ['disclosure-type', 'origin', 'originating-organization',
                     'exploitation-technique', 'domain-category', 'email-type',
                     'ip-category', 'maliciousness', 'malware-category', 'misusage-type',
                     'mitigation-type', 'scan-type', 'severity', 'threat-vector']

skip_for_now = []

ignore = ['dos-type', 'report-state', 'ftp-type', 'record-type', 'host-category',
          'method-match']

for propertytype in ontology['propertyTypes']:
    if 'accepts' in propertytype and propertytype['accepts']['name'] != 'list':
        continue
    misp_name = propertytype['name'].lower().replace('_', '-').replace(' ', '-')
    if misp_name in ignore or misp_name in skip_for_now:
        continue
    if misp_name not in predicate_of_cccs:
        new_taxonomy = Taxonomy()
        new_taxonomy.name = misp_name
        new_taxonomy.description = propertytype['description']
        new_taxonomy.version = 1
        new_taxonomy.expanded = propertytype['name'].lower().replace('_', ' ').capitalize()
        new_taxonomy.predicates = {}
        for value in propertytype['accepts']['values']:
            predicate = Predicate()
            predicate.predicate = value['name'].lower().replace('_', '-').replace(' ', '-')
            predicate.expanded = value['name'].lower().replace('_', ' ').capitalize()
            predicate.description = value['description']
            new_taxonomy.predicates[predicate.predicate] = predicate
    else:
        predicate = Predicate()
        predicate.predicate = misp_name
        predicate.expanded = propertytype['name'].lower().replace('_', ' ').capitalize()
        predicate.description = propertytype['description']
        predicate.entries = {}
        for value in propertytype['accepts']['values']:
            entry = Entry()
            entry.value = value['name'].lower().replace('_', '-').replace(' ', '-')
            entry.expanded = value['name'].lower().replace('_', ' ').capitalize()
            entry.description = value['description']
            predicate.entries[entry.value] = entry
        cccs.predicates[predicate.predicate] = predicate

    if not (root_dir_taxonomies / new_taxonomy.name).exists():
        (root_dir_taxonomies / new_taxonomy.name).mkdir()

    if (root_dir_taxonomies / new_taxonomy.name / 'machinetag.json').exists():
        with open(root_dir_taxonomies / new_taxonomy.name / 'machinetag.json') as f:
            existing_taxonomy = json.load(f)
        if existing_taxonomy == new_taxonomy.to_dict():
            continue
        new_taxonomy.version = existing_taxonomy['version'] + 1
    with open(root_dir_taxonomies / new_taxonomy.name / 'machinetag.json', 'w') as f:
        json.dump(new_taxonomy.to_dict(), f, indent=2)


# Dump generic CCCS taxonomy

if not (root_dir_taxonomies / cccs.name).exists():
    (root_dir_taxonomies / cccs.name).mkdir()

if (root_dir_taxonomies / cccs.name / 'machinetag.json').exists():
    with open(root_dir_taxonomies / cccs.name / 'machinetag.json') as f:
        existing_taxonomy = json.load(f)
    if existing_taxonomy != cccs.to_dict():
        cccs.version = existing_taxonomy['version'] + 1

with open(root_dir_taxonomies / cccs.name / 'machinetag.json', 'w') as f:
    json.dump(cccs.to_dict(), f, indent=2)
