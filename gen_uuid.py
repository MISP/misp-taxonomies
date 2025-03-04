import uuid
import os
import json

CONFIG_FILES = ["schema_mapping.json", "schema.json", "MANIFEST.json", "mapping.json"]

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".json") and filename not in CONFIG_FILES:
            print(f"open file {root}/{filename}")
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as file:
                content = json.load(file)

            # Create namespace UUID
            ns_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, content["namespace"])
            content["uuid"] = str(ns_uuid)

            # Create predicate UUID
            pred_uuid_map = {}
            for i, predicate in enumerate(content["predicates"]):
                name = f"{content['namespace']}:{content['predicates'][i]['value']}"
                predicate_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, name)
                content["predicates"][i]["uuid"] = str(predicate_uuid)
                pred_uuid_map[content["predicates"][i]["value"]] = predicate_uuid

            # Create value UUID
            try:
                for i, value in enumerate(content["values"]):
                    for j, entry in enumerate(content["values"][i]["entry"]):
                        name = f"{content['namespace']}:{content['values'][i]['predicate']}=\"{content['values'][i]['entry'][j]['value']}\""
                        puuid = pred_uuid_map[content["values"][i]["predicate"]]
                        content["values"][i]["entry"][j]["uuid"] = str(
                            uuid.uuid5(uuid.NAMESPACE_DNS, name)
                        )
            except Exception as e:
                print(f"Exception: {e}")
                pass

            with open(filepath, 'w') as file:
                json.dump(content, file, indent=4)
