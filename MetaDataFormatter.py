# MetaDataFormatter.py
# Purpose: Ensures every tool file includes standard metadata blocks — injected from a master template

import os
import uuid

META_BLOCK = '''\n# METADATA
# ScriptID: {}
# ChainLink: true
# TestScript: true
# QTLHook: true
# METADATA END\n'''

def inject_metadata(file_path):
    uid = str(uuid.uuid4())
    with open(file_path, "a") as f:
        f.write(META_BLOCK.format(uid))

def format_all():
    for root, _, files in os.walk("WorldBuilder_Suite/tools/"):
        for f in files:
            if f.endswith(".py") and "TestHarness" not in root:
                inject_metadata(os.path.join(root, f))
    print("[✓] Metadata injected.")

if __name__ == "__main__":
    format_all()

