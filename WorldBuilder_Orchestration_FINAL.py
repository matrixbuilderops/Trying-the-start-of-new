#!/usr/bin/env python3

import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

BABY_SCRIPTS = [
    "Command Flag Integrity Checker.py",
    "CommandInterfaceRegenerator.py",
    "Condenser.py",
    "File Role Verifier.py",
    "Health Monitor Script.py",
    "ImportNormalizer.py",
    "Metadata Refinery.py",
    "QTL Consistency Auditor.py",
    "QTLIdentifiers.py",
    "Recursive Hook Realigner.py",
    "TestHarnessBinder.py",
    "Toolset Upgrader Relay.py",
    "Universal Import Synchronizer.py",
    "UpgradeApplier.py",
    "Upgrade Listener.py"
]

def run(script_name):
    path = os.path.join(SCRIPT_DIR, script_name)
    if not os.path.isfile(path):
        print(f"[✗] Missing: {script_name}")
        return
    try:
        print(f"▶ Running: {script_name}")
        subprocess.run(["python3", path], check=True)
        print(f"✓ Success: {script_name}\n")
    except subprocess.CalledProcessError as e:
        print(f"[!!] Failed: {script_name} → {e}\n")

def main():
    print("🔁 Beginning WorldBuilder Orchestration")
    for script in BABY_SCRIPTS:
        run(script)
    print("\n✅ All scripts executed.")

if __name__ == "__main__":
    main()

