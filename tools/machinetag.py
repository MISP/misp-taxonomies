#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Python script parsing the MISP taxonomies expressed in Machine Tags (Triple
# Tags) to list all valid tags from a specific taxonomy.
#
# Copyright (c) 2015-2022 Alexandre Dulaunoy - a@foo.be
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
import os
import sys

skip_list = ["death-possibilities", "poison-taxonomy", "doping-substances"]
taxonomies = []

# Get our current directory from file location
thisDir = os.path.dirname(__file__)

argParser = argparse.ArgumentParser(
    description="Dump Machine Tags (Triple Tags) from MISP taxonomies",
    epilog="Available taxonomies are {0}".format(taxonomies),
)
argParser.add_argument("-e", action="store_true", help="Include expanded tags")
argParser.add_argument(
    "-a", action="store_true", help="Generate asciidoctor document from MISP taxonomies"
)
argParser.add_argument("-v", action="store_true", help="Include descriptions")
argParser.add_argument("-n", default=False, help="Show only the specified namespace")
argParser.add_argument(
    "--disable-skip-list",
    default=False,
    action="store_true",
    help="disable default skip list",
)
args = argParser.parse_args()

if args.disable_skip_list:
    skip_list = ""

for folder in os.listdir(os.path.join(thisDir, "../")):
    if os.path.isfile(os.path.join(thisDir, "../", folder, "machinetag.json")):
        if folder in skip_list:
            continue
        taxonomies.append(folder)

taxonomies.sort()


doc = ""
if args.a:
    dedication = "\n[dedication]\n== Funding and Support\nThe MISP project is financially and resource supported by https://www.circl.lu/[CIRCL Computer Incident Response Center Luxembourg ].\n\nimage:{images-misp}logo.png[CIRCL logo]\n\nA CEF (Connecting Europe Facility) funding under CEF-TC-2016-3 - Cyber Security has been granted from 1st September 2017 until 31th August 2019 as ***Improving MISP as building blocks for next-generation information sharing***.\n\nimage:{images-misp}en_cef.png[CEF funding]\n\nIf you are interested to co-fund projects around MISP, feel free to get in touch with us.\n\n"
    doc = doc + ":toc: right\n"
    doc = doc + ":toclevels: 1\n"
    doc = doc + ":icons: font\n"
    doc = (
        doc
        + ":images-cdn: https://raw.githubusercontent.com/MISP/MISP/2.4/INSTALL/logos/\n"
    )
    doc = doc + ":images-misp: https://www.misp-project.org/assets/images/\n"
    doc = doc + "= MISP taxonomies and classification as machine tags\n\n"
    doc = doc + "= Introduction\n"
    doc = doc + "\nimage::{images-cdn}misp-logo.png[MISP logo]\n"
    doc = (
        doc
        + "The MISP threat sharing platform is a free and open source software helping information sharing of threat intelligence including cyber security indicators, financial fraud or counter-terrorism information. The MISP project includes multiple sub-projects to support the operational requirements of analysts and improve the overall quality of information shared.\n\n"
    )
    doc = doc + ""
    doc = "{} {} {} {}".format(
        doc,
        "\nTaxonomies that can be used in MISP (2.4) and other information sharing tool and expressed in Machine Tags (Triple Tags).",
        "A machine tag is composed of a namespace (MUST), a predicate (MUST) and an (OPTIONAL) value.",
        "Machine tags are often called triple tag due to their format.\n",
    )
    doc = (
        doc
        + "The following document is generated from the machine-readable JSON describing the https://github.com/MISP/misp-taxonomies[MISP taxonomies]."
    )
    doc = doc + "\n\n"
    doc = doc + "<<<\n"
    doc = doc + dedication
    doc = doc + "<<<\n"
    doc = doc + "= MISP taxonomies\n"
    doc = doc + "\n\n"

if args.n:
    del taxonomies[:]
    taxonomies.append(args.n)


def asciidoc(content=False, adoc=doc, t="title", toplevel=False):
    if not args.a:
        return False
    adoc = adoc + "\n"
    if t == "title":
        content = "==== " + content
    elif t == "predicate":
        content = "=== " + content
    elif t == "namespace":
        content = "== " + content + "\n"
        content = "{}\n{}{} {}{}{} {}".format(
            content,
            "NOTE: ",
            namespace,
            "namespace available in JSON format at https://github.com/MISP/misp-taxonomies/blob/main/",
            namespace,
            "/machinetag.json[*this location*]. The JSON format can be freely reused in your application",
            "or automatically enabled in https://www.github.com/MISP/MISP[MISP] taxonomy.",
        )
    elif t == "description" and toplevel is True:
        content = "\n{} \n".format(content)
    elif t == "description" and toplevel is False:
        try:
            (n, value) = content.split(":", 1)
            content = "\n{} \n".format(value)
        except:
            content = "\n{} \n".format(content)
    elif t == "numerical_value":
        (n, value) = content.split(":", 1)
        content = '\nAssociated numerical value="{}" \n'.format(value)
    elif t == "exclusive":
        (n, value) = content.split(":", 1)
        if n:
            content = "\nIMPORTANT: Exclusive flag set which means the values or predicate below must be set exclusively.\n"
    adoc = adoc + content
    return adoc


def machineTag(namespace=False, predicate=False, value=None):

    if namespace is False or predicate is False:
        return None
    if value is None:
        return "{0}:{1}".format(namespace, predicate)
    else:
        return '{0}:{1}="{2}"'.format(namespace, predicate, value)


for taxonomy in taxonomies:
    if taxonomy in skip_list:
        sys.stderr.write(f"Skip {taxonomy}")
        continue
    filename = os.path.join(thisDir, "../", taxonomy, "machinetag.json")
    with open(filename) as fp:
        t = json.load(fp)
    namespace = t["namespace"]
    if t.get("expanded"):
        expanded_namespace = t["expanded"]
    else:
        expanded_namespace = namespace
    if args.a:
        doc = asciidoc(content=t["namespace"], adoc=doc, t="namespace")
        doc = asciidoc(
            content=t["description"], adoc=doc, t="description", toplevel=True
        )
        if t.get("exclusive"):
            doc = asciidoc(
                content=machineTag(namespace=namespace, predicate=t["exclusive"]),
                adoc=doc,
                t="exclusive",
            )
    if args.v:
        print("{0}".format(t["description"]))
    for predicate in t["predicates"]:
        if args.a:
            doc = asciidoc(content=predicate["value"], adoc=doc, t="predicate")
            if predicate.get("description"):
                doc = asciidoc(
                    content=machineTag(
                        namespace=namespace, predicate=predicate["description"]
                    ),
                    adoc=doc,
                    t="description",
                )
            if predicate.get("exclusive"):
                doc = asciidoc(
                    content=machineTag(
                        namespace=namespace, predicate=predicate["exclusive"]
                    ),
                    adoc=doc,
                    t="exclusive",
                )

        if t.get("values") is None:
            if args.a:
                doc = asciidoc(
                    content=machineTag(
                        namespace=namespace, predicate=predicate["value"]
                    ),
                    adoc=doc,
                )
                doc = asciidoc(
                    content=machineTag(
                        namespace=namespace, predicate=predicate["expanded"]
                    ),
                    adoc=doc,
                    t="description",
                )
                if predicate.get("description"):
                    doc = asciidoc(
                        content=machineTag(
                            namespace=namespace, predicate=predicate["description"]
                        ),
                        adoc=doc,
                        t="description",
                    )
                if predicate.get("numerical_value"):
                    doc = asciidoc(
                        content=machineTag(
                            namespace=namespace, predicate=predicate["numerical_value"]
                        ),
                        adoc=doc,
                        t="description",
                    )
                if predicate.get("exclusive"):
                    doc = asciidoc(
                        content=machineTag(
                            namespace=namespace, predicate=predicate["exclusive"]
                        ),
                        adoc=doc,
                        t="exclusive",
                    )
            else:
                print(machineTag(namespace=namespace, predicate=predicate["value"]))
            if args.e:
                print(
                    "--> "
                    + machineTag(
                        namespace=expanded_namespace, predicate=predicate["expanded"]
                    )
                )
                if predicate.get("description"):
                    print("--> " + predicate["description"])
        else:
            for e in t["values"]:
                if e["predicate"] == predicate["value"]:
                    if "expanded" in predicate:
                        expanded = predicate["expanded"]
                    for v in e["entry"]:
                        if args.a and "expanded" in v:
                            doc = asciidoc(
                                content=machineTag(
                                    namespace=namespace,
                                    predicate=e["predicate"],
                                    value=v["value"],
                                ),
                                adoc=doc,
                            )
                            doc = asciidoc(
                                content=machineTag(
                                    namespace=namespace, predicate=v["expanded"]
                                ),
                                adoc=doc,
                                t="description",
                            )
                            if "description" in v:
                                doc = asciidoc(
                                    content=machineTag(
                                        namespace=namespace, predicate=v["description"]
                                    ),
                                    adoc=doc,
                                    t="description",
                                )
                            if v.get("numerical_value"):
                                doc = asciidoc(
                                    content=machineTag(
                                        namespace=namespace,
                                        predicate=v["numerical_value"],
                                    ),
                                    adoc=doc,
                                    t="numerical_value",
                                )
                        else:
                            print(
                                machineTag(
                                    namespace=namespace,
                                    predicate=e["predicate"],
                                    value=v["value"],
                                )
                            )
                        if args.e:
                            if "expanded" in v:
                                print(
                                    "--> "
                                    + machineTag(
                                        namespace=namespace,
                                        predicate=expanded,
                                        value=v["expanded"],
                                    )
                                )

with open("../mapping/mapping.json") as mapping:
    m = json.load(mapping)
    output = "\n= Mapping of taxonomies\n"
    output = "{}{}".format(
        output,
        "Analysts relying on taxonomies don't always know the appropriate namespace to use but know which value to use for classification. The MISP mapping taxonomy allows to map a single classification into a series of machine-tag synonyms.\n",
    )
    for value in sorted(m.keys()):
        output = "{}{} **{}**{}{}\n".format(
            output, "\n.Mapping table - ", value, "\n|===\n|", value
        )
        for mapped in m[value]["values"]:
            output = "{}|{}\n".format(output, mapped)
        output = "{}|===\n".format(output)
    doc = doc + output

if args.a:
    print(doc)
