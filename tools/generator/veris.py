import json

debug = False
filename = 'verisc-labels.json'
namespace = 'veris'
description = 'Vocabulary for Event Recording and Incident Sharing (VERIS)'

output = {}
output['namespace'] = namespace
output['description'] = description
output['version'] = 2
output['predicates'] = []
output['values'] = []

with open(filename) as fp:
    t = json.load(fp)


def lookupPredicate(predicate=False):
    if not predicate:
        return False
    for p in output['predicates']:
        if p['value'] == predicate:
            return True


def lookupValues(predicate=False):
    if not predicate:
        return {}
    for p in output['values']:
        if p['predicate'] == predicate:
            return p
    return {}


def machineTag(namespace=False, predicate=False, value=None, expanded=None):

    if namespace is False or predicate is False:
        return None
    if value is None:
        return ('{0}:{1}'.format(namespace, predicate))
    else:
        if not lookupPredicate(predicate=predicate):
            x = {}
            x['value'] = predicate
            output['predicates'].append(x)
        z = {}
        z['value'] = value
        z['expanded'] = expanded
        predicate_entries = lookupValues(predicate)
        if predicate_entries:
            predicate_entries['entry'].append(z)
        else:
            y = {}
            y['predicate'] = predicate
            y['entry'] = []
            y['entry'].append(z)
            output['values'].append(y)
        return ('{0}:{1}=\"{2}\"'.format(namespace, predicate, value))


prefix = []
top = []


def flatten(root, prefix_keys=True):
    dicts = [([], root)]
    ret = {}
    seen = set()
    for path, d in dicts:
        if id(d) in seen:
            continue
        seen.add(id(d))
        for k, v in sorted(d.items()):
            new_path = path + [k]
            prefix = ':'.join(new_path) if prefix_keys else k
            if hasattr(v, 'items'):
                dicts.append((new_path, v))
            else:
                p = ':'.join(prefix.rsplit(':')[:-1])
                if debug:
                    print(namespace + ":" + p + "=" + v)
                machineTag(namespace=namespace, predicate=p, value=prefix.split(':')[-1], expanded=v)
                ret[prefix] = v
    return ret


flatten(root=t)

print(json.dumps(output))
