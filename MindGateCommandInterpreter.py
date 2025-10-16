
import os
import json

LOGS_DIR = "Logs/"
OUTPUT_DIR = "Output/"
CHAINLINK_REGISTRY = "Configuration/ChainLinkRegistry.json"
TOOLS_DIR = "Tools/"

def run_diagnostic_for(tool):
    diag_path = os.path.join(OUTPUT_DIR, tool, "diagnostic.json")
    if not os.path.exists(diag_path):
        print(f"⚠️ No diagnostics found for '{tool}'")
        return
    with open(diag_path, 'r') as f:
        try:
            data = json.load(f)
            print(f"📋 Diagnostics for {tool}:")
            print(json.dumps(data, indent=2))
        except Exception as e:
            print(f"❌ Error reading diagnostics: {e}")

def list_tools():
    try:
        tool_dirs = [name for name in os.listdir(TOOLS_DIR) if os.path.isdir(os.path.join(TOOLS_DIR, name))]
        print("🛠 Installed tools:")
        for t in tool_dirs:
            print(f" - {t}")
    except Exception as e:
        print(f"❌ Could not list tools: {e}")

def list_chainlinks():
    try:
        with open(CHAINLINK_REGISTRY, 'r') as f:
            data = json.load(f)
            print("🔗 ChainLink Registry:")
            print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"❌ Could not read ChainLink registry: {e}")

def main():
    print("\n🧠 MindGate Interactive Shell (v1.0)")
    print("Type structured commands like:")
    print(" DIAGNOSE: Fixer")
    print(" LIST: Tools")
    print(" LIST: ChainLinks")
    print(" REPAIR: (reserved for future)\n")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting MindGate.")
            break
        elif user_input.upper().startswith("DIAGNOSE:"):
            tool = user_input.split(":", 1)[1].strip()
            run_diagnostic_for(tool)
        elif user_input.upper() == "LIST: TOOLS":
            list_tools()
        elif user_input.upper() == "LIST: CHAINLINKS":
            list_chainlinks()
        elif user_input.upper().startswith("REPAIR:"):
            print("⚙️ Repair command routing not yet enabled.")
        else:
            print("❓ Unknown command. Try DIAGNOSE: Fixer, LIST: Tools, or LIST: ChainLinks.")

if __name__ == "__main__":
    main()
