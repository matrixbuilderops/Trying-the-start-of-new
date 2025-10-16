import os
import json

def get_root_path():
    # Assume the current directory is already inside WorldBuilder
    return os.getcwd()

def get_chainlink_path():
    return os.path.join(get_root_path(), "Tools", "Helix", "Applications", "Configuration", "ChainLinkRegistry.json")

def generate_chainlink_registry():
    registry = {
        "GodTree": "Tools/GodTree/GodTree.py",
        "Analyzer": "Tools/Analyzer/Analyzer.py",
        "Fixer": "Tools/Fixer/Fixer.py",
        "Ascension": "Tools/Ascension/Ascension.py",
        "MindGate": "Tools/Helix/Applications/Models/MindGate/MindGate.qtl"
    }
    return registry

def verify_file_availability(path_dict):
    print("🔍 Verifying file availability...")
    for name, path in path_dict.items():
        full_path = os.path.join(get_root_path(), path)
        if os.path.exists(full_path):
            print(f"✅ {name}: FOUND at {full_path}")
        else:
            print(f"❌ {name}: MISSING at {full_path}")

def write_registry(registry, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(registry, f, indent=4)
    print(f"
📁 ChainLink Registry written to: {filepath}")

if __name__ == "__main__":
    print("🔗 Initializing ChainLink Engine...")
    registry = generate_chainlink_registry()
    verify_file_availability(registry)
    chainlink_file = get_chainlink_path()
    write_registry(registry, chainlink_file)
