import json
import os
import re

filename = os.path.join("../", "MANIFEST.json")
with open(filename) as fp:
    t = json.load(fp)

for taxo in sorted(t['taxonomies'], key=lambda k: k['name']):
    print("### {}".format(taxo['name']))
    print()
    print("[{}](https://github.com/MISP/misp-taxonomies/tree/main/{}) :\n{} [Overview](https://www.misp-project.org/taxonomies.html#_{})\n".format(taxo['name'], taxo['name'], taxo['description'], re.sub(r'-', '_',taxo['name'].lower())))
