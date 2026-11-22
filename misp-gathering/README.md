# MISP Gathering Origin

Record how an event was collected by a MISP gathering module. The namespace is
`misp-gathering`, with two event-level predicates:

| Predicate | Meaning | Values |
| --- | --- | --- |
| `module` | Collector identifier advertised by misp-modules | `withaname`, `beaconbeagle_gathering`, `offensive_agency` |
| `source` | Canonical domain of the upstream data provider | `witha.name`, `beaconbeagle.com`, `offensive.agency` |

WithAName events receive:

```text
misp-gathering:module="withaname"
misp-gathering:source="witha.name"
```

BeaconBeagle configuration, beacon and C2 events receive:

```text
misp-gathering:module="beaconbeagle_gathering"
misp-gathering:source="beaconbeagle.com"
```

Offensive Agency statistics and monitored asset events carry the following tags.

```text
misp-gathering:module="offensive_agency"
misp-gathering:source="offensive.agency"
```

These tags describe collection provenance. They do not indicate confidence,
human review, the event's creator organisation or ownership of the systems
described in an event. The source is the upstream provider, not a victim domain
or an observed C2 domain. Retrieval URLs and timestamps belong in the event's
source references and observations, not in the taxonomy vocabulary.

Gathering producers should attach these as **local event tags** by including
`local: true` in each event `Tag` entry:

```json
{
  "Tag": [
    {"name": "misp-gathering:module=\"withaname\"", "local": true},
    {"name": "misp-gathering:source=\"witha.name\"", "local": true}
  ]
}
```

The taxonomy defines names and descriptions; it does not enforce locality.
Locality is a property of the event/tag association in MISP. Local tags are
visible and filterable on the importing instance and excluded from ordinary
outgoing synchronisation; internal sync can include them. Enabling the taxonomy
makes its descriptions available in the tag picker. Importing unknown tags
remains subject to the importing user's permissions.

Add module and source entries when introducing another gathering producer.
Use the exact discovery identifier for `module` and a stable canonical domain
for `source`. Neither predicate is exclusive, allowing an event to retain
multiple collection origins when appropriate.
