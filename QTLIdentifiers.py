# Metadata Refinery — Fully Compliant Version
# Refines and normalizes metadata across all tools in the directory.
# Adds embedded hooks, QTLIdentifiers, and integrity scaffolding.

import os
import hashlib
import json
from datetime import datetime

TARGET_EXTENSIONS = ['.qtl', '.py']
HOOK_IDENTIFIER = 'Hook:TestHarness'
QTL_IDENTIFIER_PREFIX = 'QTLID-'

def generate_qtl_identifier(path):
    hasher = hashlib.sha256()
    hasher.update(path.encode('utf-8'))
    return QTL_IDENTIFIER_PREFIX + hasher.hexdigest()[:16]

def refine_metadata_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    meta_block_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('#META-BEGIN'):
            meta_block_start = i
            break

    metadata = {
        "Tool": os.path.basename(file_path),
        "Version": "1.0.0",
        "QTLIdentifier": generate_qtl_identifier(file_path),
        "LastUpdated": datetime.now().isoformat(),
        "Hook": HOOK_IDENTIFIER,
        "ChainLink": True,
        "Encrypted": False,
        "SelfContained": True
    }

    meta_json = json.dumps(metadata, indent=2)

    if meta_block_start is not None:
        end_idx = next((j for j in range(meta_block_start+1, len(lines)) if lines[j].strip().startswith('#META-END')), None)
        if end_idx is not None:
            lines = lines[:meta_block_start+1] + [meta_json + "\n"] + lines[end_idx:]
        else:
            lines = lines[:meta_block_start+1] + [meta_json + "\n", "#META-END\n"]
    else:
        lines = ["#META-BEGIN\n", meta_json + "\n", "#META-END\n"] + lines

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def walk_and_refine(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                refine_metadata_in_file(os.path.join(root, file))

if __name__ == "__main__":
    walk_and_refine(".")

