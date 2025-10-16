import os
import json

def refine_metadata(directory):
    print(f"🛠️ Refining metadata in: {directory}")
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                modified = False

                # Normalize metadata fields
                if "meta" in data:
                    meta = data["meta"]

                    # Rename fields if needed
                    if "isvalid" in meta:
                        meta["isValid"] = meta.pop("isvalid")
                        modified = True
                    if "refcount" in meta:
                        meta["referenceCount"] = meta.pop("refcount")
                        modified = True

                    # Enforce string types
                    if "toolVersion" in meta and not isinstance(meta["toolVersion"], str):
                        meta["toolVersion"] = str(meta["toolVersion"])
                        modified = True

                if modified:
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"✅ Refined: {filename}")

            except Exception as e:
                print(f"⚠️ Failed to refine {filename}: {e}")

if __name__ == "__main__":
    target_dir = "./Helix/metadata"
    refine_metadata(target_dir)

