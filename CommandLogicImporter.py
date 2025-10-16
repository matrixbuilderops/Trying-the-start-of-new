# CommandLogicImporter.py
# Purpose: Allows the user to push tool logic mappings and flags from structured Word or QTL templates.

import os

TOOL_COMMAND_DIR = "WorldBuilder_Suite/configuration/commands/"

def push_logic_to_tool(tool_name, commands, flags):
    logic_file = os.path.join(TOOL_COMMAND_DIR, f"{tool_name}_logic.qtl")
    with open(logic_file, "w") as f:
        f.write("# COMMAND DEFINITIONS\n")
        for cmd in commands:
            f.write(f"{cmd}\n")
        f.write("\n# FLAGS\n")
        for flag in flags:
            f.write(f"{flag}\n")
    print(f"[✓] Logic pushed to {tool_name}")

if __name__ == "__main__":
    # Placeholder for dynamic integration with Orchestration AI
    print("[CommandLogicImporter Ready]")

