#!/usr/bin/env python3
import json
import sys
import uuid
from pathlib import Path


def add_missing_uuids(obj):
    """
    Mutates the JSON object in place to add missing 'uuid' fields:
    - Top-level object
    - Each object in 'predicates'
    - Each entry in 'values'[*]['entry']
    """
    changed = False

    # Top-level uuid
    if isinstance(obj, dict) and "uuid" not in obj:
        obj["uuid"] = str(uuid.uuid4())
        changed = True

    # Predicates list
    predicates = obj.get("predicates")
    if isinstance(predicates, list):
        for pred in predicates:
            if isinstance(pred, dict) and "uuid" not in pred:
                pred["uuid"] = str(uuid.uuid4())
                changed = True

    # Values -> entry list
    values = obj.get("values")
    if isinstance(values, list):
        for val in values:
            if not isinstance(val, dict):
                continue
            entries = val.get("entry")
            if isinstance(entries, list):
                for entry in entries:
                    if isinstance(entry, dict) and "uuid" not in entry:
                        entry["uuid"] = str(uuid.uuid4())
                        changed = True

    return changed


def process_file(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if add_missing_uuids(data):
        # Only write back if we actually changed something
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated: {path}")
    else:
        print(f"No changes: {path}")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} FILE_OR_DIR [FILE_OR_DIR ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            for json_file in p.rglob("*.json"):
                process_file(json_file)
        elif p.is_file():
            process_file(p)
        else:
            print(f"Not found: {p}", file=sys.stderr)


if __name__ == "__main__":
    main()

