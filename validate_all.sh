#!/bin/bash

set -e
set -x

./jq_all_the_things.sh

diffs=`git status --porcelain | wc -l`

if ! [ $diffs -eq 0 ]; then
	echo "Please make sure you run ./jq_all_the_things.sh before commiting."
	exit 1
fi

directories=`ls -d */ | wc -w`
manifest_entries=`cat MANIFEST.json | jq '.taxonomies | length'`

if ! [ $((directories-2)) -eq $manifest_entries ]; then
    echo "MANIFEST isn't up-to-date."
    exit 1
fi

for dir in */machinetag.json
do
  echo -n "${dir}: "
  jsonschema -i ${dir} schema.json
  echo ''
done

jsonschema -i mapping/mapping.json schema_mapping.json
