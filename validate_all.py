import sys
import glob
import json
from jsonschema import validate

schema = json.load(open("schema.json", "r"))

for taxonomy_file in glob.glob('./*/machinetag.json'):
    print("Checking {}".format(taxonomy_file))
    taxonomy = json.load(open(taxonomy_file, "r"))
    validate(instance=taxonomy, schema=schema)

    if "values" in taxonomy:
        predicates = [predicate["value"] for predicate in taxonomy["predicates"]]
        for value in taxonomy["values"]:
            if value["predicate"] not in predicates:
                print("ERROR: Predicate `{}` is missing".format(value["predicate"]))
                sys.exit(1)