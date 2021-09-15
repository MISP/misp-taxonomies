import json
import requests

debug = False
galaxy_url = 'https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters/'
elements = ['tools.json', 'threat-actors.json']
# elements = ['threat-actor-tools.json']

taxonomy = {}
taxonomy['namespace'] = 'misp-galaxy'
taxonomy['description'] = 'Elements from the misp-galaxy as taxonomy (temporary measure)'
taxonomy['version'] = 1  # FIXME - this should be incremented manually

taxonomy['predicates'] = []
taxonomy['values'] = []


for element in elements:
    g_element = requests.get(galaxy_url + element).json()

    p_description = g_element['description']
    if element.endswith('s.json'):
        p_value = element[:-6]
    elif element.endswith('-vocabulary.json'):
        p_value = element[:-16]
    else:
        p_value = element

    taxonomy['predicates'].append({'value': p_value, 'expanded': p_description})

    t_value = {}
    t_value['predicate'] = p_value
    t_value['entry'] = []
    for g_value in g_element['values']:
        item = {}
        item['value'] = g_value['value']
        item['expanded'] = g_value['value']
        if 'description' in g_value:
            item['description'] = g_value['description']
        t_value['entry'].append(item)

        # if 'synonyms' in g_value:
        #     for g_value_synonym in g_value['synonyms']:
        #         item_s = dict(item)
        #         item_s['value'] = g_value_synonym
        #         item_s['expanded'] = g_value_synonym
        #         t_value['entry'].append(item_s)
    taxonomy['values'].append(t_value)

file_out = '../../misp-galaxy/machinetag.json'
with open(file_out, 'w') as f:
    f.write(json.dumps(taxonomy, sort_keys=True, indent=4, separators=(',', ': ')))
print("JSON saved to " + file_out)


# t = Taxonomy(taxonomy)
# with open('out-t.json', 'w') as f:
#     f.write(json.dumps(t._json(), sort_keys=True, indent=4, separators=(',', ': ')))
