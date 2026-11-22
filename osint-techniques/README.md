# OSINT Collection Techniques

This taxonomy describes **how** a piece of information was collected during an
open-source intelligence (OSINT) investigation. The existing
[`osint`](../osint) taxonomy classifies the **type of source** (blog post, news
report, pastie, ...); this taxonomy complements it by describing the specific
collection technique or tradecraft used to gather the information, so that
other analysts can understand how a piece of intelligence was obtained, assess
its reliability and reproduce the collection.

The namespace is `osint-techniques`. It is organised in **8 thematic
predicates**, each with a set of concrete collection techniques:

| Predicate | Theme | Values |
| --- | --- | --- |
| `search-engine` | Search engine techniques | `dorking`, `cached-results`, `file-metadata-search`, `search-alerting` |
| `image-video` | Image and video analysis techniques | `reverse-image-search`, `image-geolocation`, `chronolocation`, `exif-metadata` |
| `social-media` | Social media techniques | `profile-analysis`, `network-pivoting`, `sock-puppet-monitoring`, `api-harvesting`, `deleted-content-recovery` |
| `infrastructure` | Internet infrastructure techniques | `passive-dns`, `whois-history`, `certificate-transparency`, `reverse-lookup`, `infrastructure-search`, `subdomain-enumeration` |
| `archive` | Archiving techniques | `web-archive`, `paste-archive`, `repository-history` |
| `records` | Public records techniques | `company-registry`, `public-records`, `people-search`, `court-records`, `patent-search` |
| `geospatial` | Geospatial techniques | `satellite-imagery`, `flight-tracking`, `vessel-tracking`, `map-pivoting` |
| `leak-dataset` | Leaked dataset techniques | `breach-search`, `dump-analysis` |

## Usage

Tag an attribute or an event with the technique that was actually used to
collect it, for example:

```text
osint-techniques:geospatial="satellite-imagery"
osint-techniques:archive="web-archive"
osint-techniques:infrastructure="passive-dns"
```

Several predicates can be combined when several techniques were used during the
same investigation:

```text
osint:source-type="microblog-post"
osint-techniques:social-media="profile-analysis"
osint-techniques:image-video="reverse-image-search"
```

The `osint` taxonomy answers "what kind of source is this?" while
`osint-techniques` answers "how was this information collected?". The
technique tag does not indicate the reliability of the source itself, the
confidence of the analyst, or the ownership of the systems described; it only
documents the collection method so the collection can be assessed and
reproduced.

## Scope and tradecraft notes

- **Passive vs active collection**: prefer passive techniques (archives,
  passive DNS, Certificate Transparency logs, published scan databases) that do
  not interact with the target. Active techniques that probe or engage a target
  infrastructure may cross legal and authorization boundaries.
- **OSINT vs HUMINT**: this taxonomy covers open sources only. Interacting
  with or eliciting information from a human subject (interview, direct
  engagement) is HUMINT tradecraft and is deliberately **not** part of this
  taxonomy. Monitoring from a controlled account (`sock-puppet-monitoring`)
  must stay passive and respect OPSEC and applicable authorization.
- **Preservation**: when a collection may need to be verified or reproduced
  later, archive the source (`archive` predicate) at collection time.

## References

- Bellingcat how-to guides: <https://www.bellingcat.com/category/resources/how-tos/>
- OSINT Framework: <https://osintframework.com/>
- MISP taxonomies (complementary `osint` taxonomy): <https://www.misp-project.org/taxonomies.html>
