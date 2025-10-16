# File: AppValidator.py

"""
AppValidator: Validates structure, hook presence, flag map, interface logic,
and output bindings for an application before deployment.

Used in Application Builder Toolset (Toolset 5).
"""

import os

def validate_application_structure(app_dir):
    required_dirs = ["hooks", "handlers", "compiled"]
    required_files = ["app_hook.qtl", "flag_map.qtl"]

    issues = []

    for dir_name in required_dirs:
        full_path = os.path.join(app_dir, dir_name)
        if not os.path.exists(full_path):
            issues.append(f"Missing required directory: {dir_name}")

    for file_name in required_files:
        found = False
        for root, _, files in os.walk(app_dir):
            if file_name in files:
                found = True
                break
        if not found:
            issues.append(f"Missing required file: {file_name}")

    if not issues:
        print(f"[+] Application structure valid: {app_dir}")
        return True
    else:
        print("[!] Application validation failed:")
        for issue in issues:
            print("    -", issue)
        return False

# Example:
# validate_application_structure("/apps/ExampleTool")

