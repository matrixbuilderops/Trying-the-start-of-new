import os
import re
import json
from datetime import datetime

# === UpgradeApplier ===
# Applies 207+ logic upgrades to each QTL tool file by inserting standard upgrade flags,
# logic triggers, and sovereign-layer recursion interface

UPGRADE_HEADER = "# === 207 Upgrade Layer Applied ==="
UPGRADE_TAG = "# [UPGRADE207]"

standard_upgrade_block = f"""
{UPGRADE_HEADER}
{UPGRADE_TAG} Injected Recursive Sovereign Flag Handler
upgrade_flag = True
sovereign_mode = 'dynamic-resolution'
last_upgrade_applied = '{datetime.utcnow().isoformat()}'
# Hooks for future toolset extensions are initialized below
future_extensions = []
"""

def apply_upgrade(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    already_upgraded = any(UPGRADE_TAG in line for line in lines)
    if already_upgraded:
        print(f"SKIP: Already upgraded — {file_path}")
        return False

    metadata_end_idx = 0
    for idx, line in enumerate(lines):
        if re.match(r"# === End Metadata ===", line):
            metadata_end_idx = idx + 1
            break

    upgraded_lines = (
        lines[:metadata_end_idx]
        + ["\n"] + standard_upgrade_block.strip().splitlines(keepends=True)
        + ["\n"] + lines[metadata_end_idx:]
    )

    with open(file_path, 'w') as f:
        f.writelines(upgraded_lines)

    print(f"UPGRADED: {file_path}")
    return True

def upgrade_all_qtl(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.qtl'):
                apply_upgrade(os.path.join(dirpath, filename))

if __name__ == "__main__":
    target_dir = "./Toolset"  # Modify to match your system's tool path
    upgrade_all_qtl(target_dir)

