#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import argparse

argParser = argparse.ArgumentParser(description='Fixing taxonomies with missing fields')
argParser.add_argument('-f', help='Taxonomy file to fix')
argParser.add_argument('-e', action='store_true', help='Fix missing expanded values at predicate level')
argParser.add_argument('-j', action='store_true', help='Dump partial JSON')
args = argParser.parse_args()


with open(args.f, 'rb') as f:
    taxonomy = json.load(f)
    for predicate_value in taxonomy['values']:
        predicate = predicate_value['predicate']
        output = []
        for a in predicate_value['entry']:
            if 'value' in a and 'expanded' in a:
                continue
            elif 'value' in a and 'expanded' not in a:
                if args.e:
                    a['expanded'] = a['value']
                    output.append(a)
        if args.j:
            print(json.dumps(output))
