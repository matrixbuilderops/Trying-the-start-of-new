# File: AppMetaInjector.py

"""
AppMetaInjector: Injects metadata into an application before deployment.

Adds:
- Unique Tool ID
- Creator ID or Organization Tag
- Ownership Chain (version-controlled)
- Runtime Signature (hash/fingerprint)
- Validation Checksum
- Timestamp

Used in Application Builder Toolset (Toolset 5).
"""

import os
import uuid
import hashlib
import datetime
import json

def generate_tool_metadata(app_name, creator_id="XELA-Initiator", version="1.0.0"):
    metadata = {
        "tool_id": str(uuid.uuid4()),
        "app_name": app_name,
        "creator": creator_id,
        "version": version,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "signature": None,
        "checksum": None
    }
    return metadata

def hash_directory(path):
    sha = hashlib.sha256()
    for root, dirs, files in os.walk(path):
        for fname in sorted(files):
            file_path = os.path.join(root, fname)
            try:
                with open(file_path, "rb") as f:
                    while True:
                        chunk = f.read(8192)
                        if not chunk:
                            break
                        sha.update(chunk)
            except Exception:
                continue
    return sha.hexdigest()

def inject_metadata(app_dir, output_file="metadata.qtl"):
    app_name = os.path.basename(app_dir.rstrip("/\\"))
    metadata = generate_tool_metadata(app_name)

    metadata["signature"] = str(uuid.uuid5(uuid.NAMESPACE_URL, app_name + metadata["timestamp"]))
    metadata["checksum"] = hash_directory(app_dir)

    output_path = os.path.join(app_dir, output_file)
    with open(output_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"[+] Metadata injected into: {output_path}")
    return output_path

# Example:
# inject_metadata("/apps/ExampleTool")

