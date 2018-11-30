import json
import os
filename = os.path.join("../", "MANIFEST.json")
with open(filename) as fp:
	t = json.load(fp)

for taxo in sorted(t['taxonomies'], key=lambda k: k['name']):
    print ("{}:\n:   {}\n".format(taxo['name'], taxo['description']))
