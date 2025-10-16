#!/usr/bin/env python3

import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WB_DIR = os.path.join(SCRIPT_DIR, "WorldBuilder")

SCRIPT_SEQUENCE = [
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

def run_script(script_name):
    script_path = os.path.join(WB_DIR, script_name)
    if not os.path.isfile(script_path):
        print(f"[✗] Missing: {script_name} (not found at {script_path})")
        return
    try:
        print(f"▶ Running: {script_path}")
        subprocess.run(["python3", script_path], check=True)
        print(f"✓ Success: {script_name}\n")
    except subprocess.CalledProcessError as e:
        print(f"[!!] Failed: {script_name} → {e}\n")

def main():
    print(f"🔧 WorldBuilder Full Orchestration (Fully Integrated)")
    print(f"📁 Root: {WB_DIR}\n")
    for script in SCRIPT_SEQUENCE:
        run_script(script)
    print("\n✅ WorldBuilder Suite fully orchestrated.")

if __name__ == "__main__":
    main()
