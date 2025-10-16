# TestHarnessBinder.py
# Ensures every QTL file is connected to the correct central test harness

import os
import re

ROOT_DIRECTORY = "."  # Set to your QTL directory
HARNESS_PATH = "./Application/TestHarness/TestHarness.qtl"

def bind_test_harness(content: str) -> str:
    lines = content.splitlines()
    new_lines = []
    found_hook = False
    inserted = False

    for line in lines:
        if line.strip().startswith("Hook:") and HARNESS_PATH in line:
            found_hook = True
        elif line.strip().startswith("Hook:") and not inserted:
            # Insert harness hook before other hooks
            new_lines.append(f"Hook: {HARNESS_PATH}")
            inserted = True
        new_lines.append(line)

    if not found_hook and not inserted:
        # Find where to insert the hook if none were present
        for i, line in enumerate(new_lines):
            if line.strip().startswith("Use:") or line.strip().startswith("UUID:") or line.strip().startswith("QTLHook"):
                continue
            # Insert hook after metadata
            new_lines.insert(i + 1, f"Hook: {HARNESS_PATH}")
            break

    return "\n".join(new_lines)

def bind_all_files():
    for dirpath, _, filenames in os.walk(ROOT_DIRECTORY):
        for filename in filenames:
            if filename.endswith(".qtl"):
                full_path = os.path.join(dirpath, filename)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()

                updated = bind_test_harness(content)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(updated)
                print(f"Test harness bound: {full_path}")

if __name__ == "__main__":
    bind_all_files()

