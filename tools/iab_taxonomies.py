#!/usr/bin/env python3
"""Generate MISP taxonomies from IAB Tech Lab TSV taxonomy files.

The source TSV files are maintained by IAB Tech Lab in:
https://github.com/InteractiveAdvertisingBureau/Taxonomies
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

TAXONOMY_ROOT_PATH = Path(__file__).resolve().parent.parent
IAB_REPOSITORY_URL = "https://github.com/InteractiveAdvertisingBureau/Taxonomies"
IAB_LICENSE_URL = "https://creativecommons.org/licenses/by/3.0/"
UUID_NAMESPACE = uuid.UUID("6c7f2f42-5085-5f0b-9f8a-b8dd0d1bf9d5")


@dataclass(frozen=True)
class IABTaxonomy:
    namespace: str
    expanded: str
    description: str
    source: str
    version: int


TAXONOMIES = {
    "iab-content-3-1": IABTaxonomy(
        namespace="iab-content-3-1",
        expanded="IAB Tech Lab Content Taxonomy 3.1",
        description=(
            "IAB Tech Lab Content Taxonomy 3.1 converted from the official TSV. "
            "It provides a common language for describing content or the aboutness "
            "of a webpage, application, or video. Source taxonomy © IAB Tech Lab, "
            "licensed under Creative Commons Attribution 3.0."
        ),
        source="Content Taxonomies/Content Taxonomy 3.1.tsv",
        version=1,
    ),
    "iab-content-3-0-descriptive-vectors": IABTaxonomy(
        namespace="iab-content-3-0-descriptive-vectors",
        expanded="IAB Tech Lab Content Taxonomy 3.0 Descriptive Vectors",
        description=(
            "IAB Tech Lab Content Taxonomy 3.0 Descriptive Vectors converted from "
            "the official TSV. Source taxonomy © IAB Tech Lab, licensed under "
            "Creative Commons Attribution 3.0."
        ),
        source="Content Taxonomies/Content Taxonomy 3.0 Descriptive Vectors.tsv",
        version=1,
    ),
    "iab-audience-1-1": IABTaxonomy(
        namespace="iab-audience-1-1",
        expanded="IAB Tech Lab Audience Taxonomy 1.1",
        description=(
            "IAB Tech Lab Audience Taxonomy 1.1 converted from the official TSV. "
            "It provides common nomenclature for audience segment names to improve "
            "comparability across data providers. Source taxonomy © IAB Tech Lab, "
            "licensed under Creative Commons Attribution 3.0."
        ),
        source="Audience Taxonomies/Audience Taxonomy 1.1.tsv",
        version=1,
    ),
    "iab-ad-product-2-0": IABTaxonomy(
        namespace="iab-ad-product-2-0",
        expanded="IAB Tech Lab Ad Product Taxonomy 2.0",
        description=(
            "IAB Tech Lab Ad Product Taxonomy 2.0 converted from the official TSV. "
            "It establishes standardized nomenclature for describing the product or "
            "service advertised within a creative unit. Source taxonomy © IAB Tech "
            "Lab, licensed under Creative Commons Attribution 3.0."
        ),
        source="Ad Product Taxonomies/Ad Product Taxonomy 2.0.tsv",
        version=1,
    ),
}


def slugify(value: str) -> str:
    value = value.strip().lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "undefined"


def stable_uuid(*parts: str) -> str:
    return str(uuid.uuid5(UUID_NAMESPACE, "::".join(parts)))


def normalize_header(header: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", header.lower()).strip()


def pick_column(headers: Iterable[str], candidates: Iterable[str]) -> str | None:
    normalized = {normalize_header(header): header for header in headers}
    for candidate in candidates:
        header = normalized.get(normalize_header(candidate))
        if header is not None:
            return header
    return None


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in csv.DictReader(handle, dialect="excel-tab")
        ]


def tier_columns(headers: Iterable[str]) -> list[str]:
    tiers = []
    for header in headers:
        if re.fullmatch(r"\s*tier\s+\d+\s*", header, re.IGNORECASE):
            tiers.append(header)
    return sorted(tiers, key=lambda header: int(re.search(r"\d+", header).group(0)))


def row_label(row: dict[str, str], tiers: list[str], name_column: str | None) -> str:
    if name_column and row.get(name_column):
        return row[name_column]
    for tier in reversed(tiers):
        if row.get(tier):
            return row[tier]
    return ""


def row_path(row: dict[str, str], tiers: list[str], label: str) -> list[str]:
    path = [row[tier] for tier in tiers if row.get(tier)]
    if path:
        return path
    return [label]


def generate_taxonomy(config: IABTaxonomy, source_file: Path) -> dict:
    rows = read_tsv(source_file)
    if not rows:
        raise ValueError(f"{source_file} does not contain TSV rows")

    headers = rows[0].keys()
    tiers = tier_columns(headers)
    if not tiers:
        raise ValueError(f"{source_file} does not contain Tier columns")

    id_column = pick_column(headers, ["Unique ID", "Relational ID", "ID"])
    parent_column = pick_column(headers, ["Parent", "Parent ID"])
    name_column = pick_column(headers, ["Name", "Condensed Name (1st, 2nd, Last Tier)", "Vector"])
    note_column = pick_column(headers, ["Extension Notes", "*Extension Notes", "Notes", "Description"])

    predicates_by_value: dict[str, dict] = {}
    entries_by_predicate: dict[str, list[dict]] = {}

    for row in rows:
        label = row_label(row, tiers, name_column)
        if not label:
            continue
        path = row_path(row, tiers, label)
        top_label = path[0]
        predicate_value = slugify(top_label)
        predicates_by_value.setdefault(
            predicate_value,
            {
                "value": predicate_value,
                "expanded": top_label,
                "description": f"IAB top-level category: {top_label}.",
                "uuid": stable_uuid(config.namespace, "predicate", predicate_value),
            },
        )

        # Top-tier rows become predicates. More specific rows become values under
        # their top-tier predicate.
        if len(path) == 1 and label == top_label:
            continue

        entry_value = slugify(" ".join(path[1:]) or label)
        expanded = " / ".join(path)
        description_bits = [expanded]
        if id_column and row.get(id_column):
            description_bits.append(f"IAB Unique ID: {row[id_column]}")
        if parent_column and row.get(parent_column):
            description_bits.append(f"IAB Parent ID: {row[parent_column]}")
        if note_column and row.get(note_column):
            description_bits.append(row[note_column])

        entries_by_predicate.setdefault(predicate_value, []).append(
            {
                "value": entry_value,
                "expanded": expanded,
                "description": "; ".join(description_bits) + ".",
                "uuid": stable_uuid(config.namespace, "entry", predicate_value, entry_value, row.get(id_column, "")),
            }
        )

    predicates = sorted(predicates_by_value.values(), key=lambda item: item["value"])
    values = []
    for predicate in predicates:
        entries = entries_by_predicate.get(predicate["value"])
        if entries:
            # Keep source order while removing duplicate tag values within each predicate.
            seen = set()
            unique_entries = []
            for entry in entries:
                if entry["value"] in seen:
                    continue
                seen.add(entry["value"])
                unique_entries.append(entry)
            values.append({"predicate": predicate["value"], "entry": unique_entries})

    taxonomy = {
        "namespace": config.namespace,
        "expanded": config.expanded,
        "description": config.description,
        "version": config.version,
        "refs": [IAB_REPOSITORY_URL, IAB_LICENSE_URL],
        "predicates": predicates,
    }
    if values:
        taxonomy["values"] = values
    return taxonomy


def write_taxonomy(taxonomy: dict, output_root: Path) -> Path:
    output_dir = output_root / taxonomy["namespace"]
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "machinetag.json"
    with output_file.open("w", encoding="utf-8") as handle:
        json.dump(taxonomy, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return output_file


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--iab-repo",
        type=Path,
        required=True,
        help="Path to a checkout of https://github.com/InteractiveAdvertisingBureau/Taxonomies",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=TAXONOMY_ROOT_PATH,
        help="Repository root where generated MISP taxonomy directories are written.",
    )
    parser.add_argument(
        "--taxonomy",
        choices=sorted(TAXONOMIES),
        action="append",
        help="Generate only this taxonomy. Can be specified multiple times.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    selected = args.taxonomy or sorted(TAXONOMIES)
    output_root = args.output_root.resolve()
    source_root = args.iab_repo.resolve()

    for name in selected:
        config = TAXONOMIES[name]
        source_file = source_root / config.source
        if not source_file.exists():
            print(f"Missing source TSV: {source_file}", file=sys.stderr)
            return 1
        output_file = write_taxonomy(generate_taxonomy(config, source_file), output_root)
        print(f"Generated {output_file.relative_to(output_root)} from {source_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
