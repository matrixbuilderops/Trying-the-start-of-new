# QTLHookInjector.py
# Purpose: Injects runtime execution hooks into files to prepare for orchestration via the QTL interface

import os

def inject_qtl_hook(file_path):
    hook = "\n# QTL EXECUTION HOOK\nUse: QTL -> Execute main()\n"
    with open(file_path, "a") as f:
        f.write(hook)

def process():
    for root, _, files in os.walk("WorldBuilder_Suite/tools/"):
        for f in files:
            if f.endswith(".py") and "TestHarness" not in root:
                inject_qtl_hook(os.path.join(root, f))
    print("[✓] QTL Hooks injected.")

if __name__ == "__main__":
    process()

