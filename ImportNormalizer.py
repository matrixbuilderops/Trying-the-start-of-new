# ImportNormalizer.py
# Normalizes import statements across all QTL files in the toolset

import os
import re

ROOT_DIRECTORY = "."  # Adjust if your toolset lives in a subfolder
STANDARD_IMPORTS = [
    "Use: ./validators/*",
    "Use: ./hooks/*",
    "Use: ./configs/*"
]

def normalize_imports(content: str) -> str:
    # Remove all current 'Use:' lines
    lines = content.splitlines()
    cleaned = [line for line in lines if not line.strip().startswith("Use:")]
    
    # Inject standardized imports after metadata block
    insert_index = 1
    for i, line in enumerate(cleaned):
        if line.startswith("QTL::Meta") or "UUID:" in line:
            insert_index = i + 1
    for imp in reversed(STANDARD_IMPORTS):
        cleaned.insert(insert_index, imp)

    return "\n".join(cleaned)

def normalize_all_imports():
    for dirpath, _, filenames in os.walk(ROOT_DIRECTORY):
        for filename in filenames:
            if filename.endswith(".qtl"):
                full_path = os.path.join(dirpath, filename)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()

                updated = normalize_imports(content)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(updated)
                print(f"Imports normalized: {full_path}")

if __name__ == "__main__":
    normalize_all_imports()

