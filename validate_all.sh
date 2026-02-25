#!/bin/bash

set -e
set -x

./jq_all_the_things.sh

diffs=`git status --porcelain | grep ".json$" | wc -l`
# Check if some JSON are not JQued.
if ! [ $diffs -eq 0 ]; then
	echo "Since we run ./jq_all_the_things.sh before committing. You probably need to add some files again"
  git status
	exit 1
fi

directories=`ls -d */ | wc -w`
manifest_entries=`cat MANIFEST.json | jq '.taxonomies | length'`

if ! [ $((directories-2)) -eq $manifest_entries ]; then
    echo "MANIFEST isn't up-to-date."
    exit 1
fi

python3 validate_all.py
jsonschema -i mapping/mapping.json schema_mapping.json

echo "Generating Manifest"
cd tools
python3 gen_manifest.py
cd ..
# validate if some files are missing in the pull request.
diffs=`git status --porcelain | wc -l`
if ! [ $diffs -eq 0 ]; then
	echo "Please check if you need to add some files to your push request"
  git status
	exit 1
fi



