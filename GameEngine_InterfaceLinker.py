import os
import re

# Configuration
HELIX_BACKEND_PATH = "Backend/Helix"
GAME_ENGINE_PATH = "Applications/GameEngine"
VALID_INTERFACE_TAGS = ["inject_engine", "compile_runtime", "scan_compatibility"]

def get_hook_line(tag):
    return f"# HOOK:{tag}"

def update_interface_references(file_path, tags):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        updated_lines.append(line)
        for tag in tags:
            if get_hook_line(tag) in line:
                updated_lines.append(f'import {tag}_handler\n')

    with open(file_path, 'w') as f:
        f.writelines(updated_lines)

def scan_and_patch_game_engine():
    print("🔍 Scanning GameEngine directory...")
    for root, _, files in os.walk(GAME_ENGINE_PATH):
        for file in files:
            if file.endswith('.py') and "interface" in file.lower():
                full_path = os.path.join(root, file)
                print(f"🔧 Patching interface file: {full_path}")
                update_interface_references(full_path, VALID_INTERFACE_TAGS)

    print("✅ Interface linking complete.")

if __name__ == "__main__":
    scan_and_patch_game_engine()

