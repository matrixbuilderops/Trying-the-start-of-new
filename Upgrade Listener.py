# Upgrade Listener — Distributed System Update Processor
# Accepts upgrade signals from Ascenda and applies validated updates across linked toolsets

import os
import json
import shutil
from datetime import datetime

UPGRADE_LOG = "upgrade_log.txt"
TOOLSET_DIRECTORY = "."

def load_upgrade_package(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            package = json.load(f)
        return package
    except Exception as e:
        print(f"[!] Failed to load upgrade package: {e}")
        return None

def backup_file(file_path):
    timestamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
    backup_path = f"{file_path}.bak_{timestamp}"
    shutil.copyfile(file_path, backup_path)

def apply_upgrade_to_file(file_path, changes):
    try:
        backup_file(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for find, replace in changes.items():
            content = content.replace(find, replace)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        log_upgrade(file_path, changes)

    except Exception as e:
        print(f"[!] Upgrade failed for {file_path}: {e}")

def log_upgrade(file_path, changes):
    with open(UPGRADE_LOG, 'a', encoding='utf-8') as log:
        log.write(f"\n[{datetime.utcnow()}] Applied upgrade to {file_path}:\n")
        for find, replace in changes.items():
            log.write(f"  • Replaced '{find}' with '{replace}'\n")

def process_upgrade_package(package):
    changeset = package.get("changeset", {})
    for relative_path, changes in changeset.items():
        full_path = os.path.join(TOOLSET_DIRECTORY, relative_path)
        if os.path.exists(full_path):
            apply_upgrade_to_file(full_path, changes)
        else:
            print(f"[!] Skipped missing file: {relative_path}")

if __name__ == "__main__":
    print("Awaiting upgrade package... Place your .json upgrade file in ./upgrade.json")
    if os.path.exists("upgrade.json"):
        pkg = load_upgrade_package("upgrade.json")
        if pkg:
            process_upgrade_package(pkg)
        else:
            print("[!] No valid upgrade data found.")
    else:
        print("[!] No upgrade.json file detected.")

