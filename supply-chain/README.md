# Software Supply Chain Attacks

This taxonomy classifies **software supply chain attacks**: it describes which
**stage** of the supply chain was compromised, which **technique** was used and
which **ecosystem** was targeted. It complements the kill-chain taxonomies
(`kill-chain`, `unified-kill-chain`, `stix-ttp`, ...) which describe the general
attack lifecycle but not the specificity of supply chain compromises — a top-3
threat vector according to the ENISA Threat Landscape and OWASP Top 10 2025
(A03:2025 Software Supply Chain Failures).

The namespace is `supply-chain`. It is organised in **3 predicates**, each with
a set of concrete values:

| Predicate | Meaning | Values |
| --- | --- | --- |
| `stage` | Which link of the supply chain was compromised (SLSA source/build/provenance concerns, widened) | `source-code`, `build-system`, `ci-cd-pipeline`, `distribution`, `dependency`, `update-mechanism`, `signing-certificate` |
| `technique` | Attack technique used (MITRE ATT&CK T1195, ENISA threat landscape, OWASP A03:2025) | `typosquatting`, `dependency-confusion`, `malicious-package`, `compromised-maintainer-account`, `ci-cd-exploit`, `stolen-signing-certificate`, `build-pipeline-injection`, `slopsquatting` |
| `ecosystem` | Ecosystem / registry / distribution platform targeted | `npm`, `pypi`, `maven`, `docker-hub`, `github-actions`, `vscode-marketplace`, `other` |

## Usage

Tag an attribute or an event with the stage, technique and ecosystem of the
supply chain attack, for example a typosquatted package on npm:

```text
supply-chain:stage="dependency"
supply-chain:technique="typosquatting"
supply-chain:ecosystem="npm"
```

A compromised CI/CD pipeline delivering a backdoored build (SolarWinds-style):

```text
supply-chain:stage="ci-cd-pipeline"
supply-chain:technique="build-pipeline-injection"
supply-chain:ecosystem="github-actions"
```

A stolen code-signing certificate used to sign a malicious update:

```text
supply-chain:stage="signing-certificate"
supply-chain:technique="stolen-signing-certificate"
supply-chain:stage="update-mechanism"
```

The three predicates are **not exclusive**: several stages or techniques can be
tagged on the same event when an attack chain crosses several links of the
supply chain (e.g. a compromised maintainer account leading to a poisoned
release and a stolen certificate). Prefer the most specific stage when only one
link was actually compromised.

## Scope notes

- This taxonomy describes the **supply chain attack itself**, not the payload
  delivered: the final malware behaviour is tagged with the usual malware /
  kill-chain taxonomies, while `supply-chain` documents how it was introduced.
- `stage` describes **where** the compromise happened, `technique` describes
  **how** it was done; use both together for meaningful trend analysis.
- The `ecosystem` predicate identifies the targeted registry or platform, not
  the victim: an attack on the npm registry affects all downstream consumers.

## References

- OWASP Top 10 2025 — A03:2025 Software Supply Chain Failures: <https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/>
- SLSA (Supply-chain Levels for Software Artifacts): <https://slsa.dev/>
- ENISA Threat Landscape for Supply Chain Attacks: <https://www.enisa.europa.eu/publications/threat-landscape-for-supply-chain-attacks>
- MITRE ATT&CK T1195 Supply Chain Compromise: <https://attack.mitre.org/techniques/T1195/>
- OpenSSF (Open Source Security Foundation): <https://openssf.org/>
