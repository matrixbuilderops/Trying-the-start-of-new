import os
import json

# Paths and Constants
RUNTIME_PATH = "Runtime/CoreEngine"
BRIDGE_CONFIG_PATH = "Runtime/Config/bridge_map.json"
COMPILATION_TARGETS = ["HelixCore", "SuccessorGenerator", "RenderPipeline"]

def load_bridge_config():
    try:
        with open(BRIDGE_CONFIG_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def generate_runtime_link_code(target):
    return f"# Injected runtime bridge for {target}\nconnect_to_runtime('{target}')\n"

def apply_runtime_bridges(config):
    for target in COMPILATION_TARGETS:
        target_file = config.get(target, f"{RUNTIME_PATH}/{target}.py")
        if os.path.exists(target_file):
            with open(target_file, 'a') as f:
                f.write(generate_runtime_link_code(target))
            print(f"🔗 Linked runtime bridge: {target_file}")
        else:
            print(f"⚠️ Runtime target missing: {target_file}")

def compile_runtime_bridges():
    print("🚀 Compiling runtime bridges...")
    config = load_bridge_config()
    apply_runtime_bridges(config)
    print("✅ Runtime bridge compilation complete.")

if __name__ == "__main__":
    compile_runtime_bridges()

