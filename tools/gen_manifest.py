#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path
from datetime import datetime

TAXONOMY_ROOT_PATH = Path(__file__).resolve().parent.parent


def fetchTaxonomies():
    taxonomiesFolder = TAXONOMY_ROOT_PATH
    taxonomies = []
    allTaxonomies = list(taxonomiesFolder.glob('./*/machinetag.json'))
    allTaxonomies.sort()
    for taxonomyFile in allTaxonomies:
        with open(taxonomyFile, 'rb') as f:
            taxonomy = json.load(f)
            taxonomies.append(taxonomy)
    return taxonomies

def generateManifest(taxonomies):
    manifest = {}
    manifest['taxonomies'] = []
    manifest['path'] = 'machinetag.json'
    manifest['url'] = 'https://raw.githubusercontent.com/MISP/misp-taxonomies/main/'
    manifest['description'] = 'Manifest file of MISP taxonomies available.'
    manifest['license'] = 'CC-0'
    now = datetime.now()
    manifest['version'] = '{}{:02}{:02}'.format(now.year, now.month, now.day)
    for taxonomy in taxonomies:
        taxObj = {
            'name': taxonomy['namespace'],
            'description': taxonomy['description'],
            'version': taxonomy['version']
        }
        manifest['taxonomies'].append(taxObj)
    return manifest

def saveManifest(manifest):
    with open(TAXONOMY_ROOT_PATH / 'MANIFEST.json', 'w') as f:
        json.dump(manifest, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write('\n')

def awesomePrint(text):
    print('\033[1;32m{}\033[0;39m'.format(text))

if __name__ == "__main__":
    taxonomies = fetchTaxonomies()
    manifest = generateManifest(taxonomies)
    saveManifest(manifest)
    awesomePrint('> Manifest saved!')
