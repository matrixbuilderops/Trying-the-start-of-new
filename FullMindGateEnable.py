# FullMindGateEnable.py

import os

class MindGate:
    def __init__(self, config_path, command_path, tools_root):
        self.config_path = config_path
        self.command_path = command_path
        self.tools_root = tools_root
        self.orchestration_ai_enabled = True
        self.restricted_access = {
            'Helix': 'boss_only',
            'configuration': 'boss_only'
        }

    def scan_config(self):
        print("Scanning configuration...")
        # Reads configuration QTL-style template and pulls settings
        if not os.path.exists(self.config_path):
            print("Configuration file missing.")
            return
        with open(self.config_path, 'r') as f:
            data = f.read()
            print(f"[CONFIG SCAN] -> {len(data)} characters loaded.")

    def parse_commands(self):
        print("Parsing command file...")
        if not os.path.exists(self.command_path):
            print("Command definition file not found.")
            return
        with open(self.command_path, 'r') as f:
            data = f.read()
            print(f"[COMMAND PARSE] -> Loaded {len(data)} characters.")

    def enforce_restrictions(self, user):
        if user != 'boss':
            raise PermissionError("Only the boss may modify Helix or configuration.")

    def activate(self, user):
        self.enforce_restrictions(user)
        print("MindGate Activated.")
        self.scan_config()
        self.parse_commands()
        print("System logic propagation initialized.")

# Initialize with real paths
if __name__ == "__main__":
    gate = MindGate(
        config_path="WorldBuilder_Suite/configuration/system_config.qtl",
        command_path="WorldBuilder_Suite/tools/Helix/Backend/CommandDefinitions.qtl",
        tools_root="WorldBuilder_Suite/tools"
    )
    gate.activate(user="boss")

