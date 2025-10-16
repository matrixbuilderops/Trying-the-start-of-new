# LogicCompiler.py
# Purpose: Auto-build internal logic links, apply imports, metadata, and test/QTL hooks for all relevant scripts in the system.
# Integrates with ChainLink and Orchestration layers.

import os

TOOLSET_ROOT = "WorldBuilder_Suite/tools/"
LOGICAL_FOLDERS = ["GodTree", "Analyzer", "Fixer", "Ascension", "Helix"]
HOOK_TYPES = ["TestHarness", "QTL", "ChainLink"]

def get_all_files(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                yield os.path.join(root, file)

def apply_import_structure(file_path):
    imports = [
        "from Helix.Backend.Core import BaseModule",
        "from Helix.Applications.QTL import QTLHandler",
        "from Helix.Applications.TestHarness import run_test",
    ]
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Prevent duplicate imports
    existing = [line.strip() for line in lines if line.strip().startswith("from")]
    new_lines = [i for i in imports if i not in existing]
    updated = "\n".join(new_lines) + "\n\n" + "".join(lines)

    with open(file_path, "w") as f:
        f.write(updated)

def inject_metadata_stub(file_path):
    stub = "\n\n# METADATA START\n# This file is auto-registered by LogicCompiler\n# METADATA END\n"
    with open(file_path, "a") as f:
        f.write(stub)

def inject_hook_stub(file_path, hook_type):
    hook = f"\n\n# HOOK START [{hook_type}]\n# Registered for {hook_type} operations\n# HOOK END\n"
    with open(file_path, "a") as f:
        f.write(hook)

def compile_logic():
    for folder in LOGICAL_FOLDERS:
        folder_path = os.path.join(TOOLSET_ROOT, folder)
        for file in get_all_files(folder_path):
            apply_import_structure(file)
            inject_metadata_stub(file)
            for hook in HOOK_TYPES:
                inject_hook_stub(file, hook)
            print(f"[Linked] {file}")

if __name__ == "__main__":
    compile_logic()
    print("[✓] LogicCompiler complete.")

