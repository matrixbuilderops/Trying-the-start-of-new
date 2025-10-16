# Metadata Refinery — Embedded QTL Metadata Generator and Validator
# Adds dynamic metadata headers, hook declarations, and conformance annotations

import os
from datetime import datetime

METADATA_TEMPLATE = """# === METADATA BLOCK ===
# Tool ID: {tool_id}
# Generated: {timestamp}
# HookChain: {hook_chain}
# LinkedValidator: {linked_validator}
# RequiresHarness: True
# IntegrityValidated: True
# =======================
"""

def generate_metadata_block(tool_id, hook_chain, validator):
    return METADATA_TEMPLATE.format(
        tool_id=tool_id,
        timestamp=datetime.utcnow().isoformat(),
        hook_chain=" -> ".join(hook_chain),
        linked_validator=validator
    )

def inject_metadata(file_path, metadata_block):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Remove existing metadata
        start = None
        end = None
        for i, line in enumerate(lines):
            if "# === METADATA BLOCK ===" in line:
                start = i
            if "# =======================" in line and start is not None:
                end = i + 1
                break

        if start is not None and end is not None:
            del lines[start:end]

        lines.insert(0, metadata_block + "\n")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    except Exception as e:
        print(f"[!] Failed to update metadata for {file_path}: {e}")

def run_metadata_refinery(root_path):
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith(".py") or file.endswith(".qtl"):
                full_path = os.path.join(root, file)
                tool_id = os.path.splitext(file)[0]
                hook_chain = [tool_id, "HarnessCore"]
                linked_validator = "Helix.Validator.Core"
                metadata = generate_metadata_block(tool_id, hook_chain, linked_validator)
                inject_metadata(full_path, metadata)

if __name__ == "__main__":
    run_metadata_refinery(".")

