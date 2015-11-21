#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Python script parsing the MISP taxonomies expressed in Machine Tags (Triple
# Tags) to list all valid tags from a specific taxonomy.
#
# Copyright (c) 2015 Alexandre Dulaunoy - a@foo.be
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import os.path
import argparse

taxonomies = ['admiralty-scale']

argParser = argparse.ArgumentParser(description='Dump Machine Tags (Triple Tags) from MISP taxonomiesi')
argParser.add_argument('-e', action='store_true', help='Including expanded tags')
args = argParser.parse_args()


def machineTag(namespace=False, predicate=False, value=None):

    if namespace is False or predicate is False:
        return None
    if value is None:
        return ('{0}:{1}'.format(namespace, predicate))
    else:
        return ('{0}:{1}=\"{2}\"'.format(namespace, predicate, value))

for taxonomy in taxonomies:
    filename = os.path.join("../", taxonomy, "machinetag.json")
    with open(filename) as fp:
        t = json.load(fp)
    namespace = t['namespace']
    for predicate in t['predicates']:
        for e in t['values']:
            if e['predicate'] == predicate['value']:
                expanded = predicate['expanded']
                for v in e['entry']:
                    print (machineTag(namespace=namespace, predicate=e['predicate'], value=v['value']))
                    if args.e:
                        print ("--> " + machineTag(namespace=namespace, predicate=expanded, value=v['expanded']))
