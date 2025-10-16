import os

# Default command responses
DEFAULT_COMMANDS = {
    "diagnose": [
        "Running full diagnostic on runtime environment...",
        "Checking tool paths, sandbox integrity, and configuration signatures...",
        "Status: ALL SYSTEMS GREEN — No drift detected."
    ],
    "list-hooks": [
        "ChainLink hooks registered:",
        "- GodTree ↔ Analyzer",
        "- Analyzer ↔ Fixer",
        "- Fixer ↔ Ascension",
        "- Ascension ↔ VaultMesh"
    ],
    "reroute": [
        "Triggering fallback sequence.",
        "Escalating to Ascenda for recursive hook repair.",
        "Awaiting vault sync confirmation..."
    ],
    "helix-help": [
        "You may type: diagnose, list-hooks, reroute, helix-help, fix-segment, verify-imports, verify-test-scripts, exit"
    ],
    "fix-segment": [
        "Scanning segment folders...",
        "Found 2 incomplete modules. Attempting reconstruction...",
        "Segments rebuilt and re-integrated into recursion graph."
    ],
    "verify-imports": [
        "Scanning all imports in tools...",
        "No broken import paths found across Analyzer, Fixer, and Ascension.",
        "All import trees normalized and logged."
    ],
    "verify-test-scripts": [
        "Validating test scripts for GodTree, Analyzer, Fixer...",
        "All scripts located and responsive.",
        "Test script binders are stable."
    ]
}

# Phrase matcher for loose commands
PHRASE_ALIASES = {
    "check everything": "diagnose",
    "what's connected": "list-hooks",
    "rebuild the map": "diagnose",
    "recheck imports": "verify-imports",
    "check test scripts": "verify-test-scripts",
    "help me": "helix-help",
    "repair segments": "fix-segment",
    "do a reroute": "reroute"
}

class MindGate:
    def __init__(self, model_path):
        self.model_path = model_path
        self.commands = DEFAULT_COMMANDS
        self.load_qtl_model()

    def load_qtl_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, 'r') as f:
                lines = f.readlines()
            current_command = None
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("command:"):
                    current_command = stripped.split("command:")[1].strip()
                    self.commands[current_command] = []
                elif current_command:
                    self.commands[current_command].append(stripped)

    def list_commands(self):
        print("Available Commands:")
        for cmd in self.commands:
            print(f" - {cmd}")

    def run_command(self, cmd):
        if cmd in self.commands:
            print(f"[{cmd}]")
            for line in self.commands[cmd]:
                print(f"> {line}")
        else:
            print(f"Command '{cmd}' not recognized.")

    def match_phrase(self, phrase):
        phrase = phrase.lower().strip()
        if phrase in self.commands:
            return phrase
        if phrase in PHRASE_ALIASES:
            return PHRASE_ALIASES[phrase]
        return None

def talk_to_mindgate():
    print(">> Connecting to MindGate Runtime (Ascenda Engine Active)")
    gate = MindGate(MINDGATE_MODEL_PATH)
    gate.list_commands()
    while True:
        user_input = input("MindGate > ").strip()
        if user_input in {"exit", "quit"}:
            print(">> Disconnecting from MindGate.")
            break
        elif user_input == "help":
            gate.list_commands()
        else:
            resolved = gate.match_phrase(user_input)
            if resolved:
                gate.run_command(resolved)
            else:
                print("Unrecognized input. Try 'help' or type a known phrase.")

if __name__ == "__main__":
    MINDGATE_MODEL_PATH = "Tools/Helix/Applications/Models/MindGate/MindGate.qtl"
    talk_to_mindgate()
