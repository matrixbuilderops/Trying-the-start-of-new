# WorldBuilderOrchestration_FINAL.py

import os
import subprocess

script_order = [
    "MindGateModel.py",           # <- NEW, runs first
    "MetaDataFormatter.py",
    "QTLHookInjector.py",
    "TestScriptGenerator.py",
    "ToolTemplateScanner.py",
    "CommandLogicImporter.py",
    "LogicCompiler.py",
    "FullMindGateEnable.py",
    "ChainLinkEngine.py"
]

def run_script(script_name):
    script_path = os.path.join(os.getcwd(), script_name)
    if not os.path.isfile(script_path):
        print(f"[ERROR] Script not found: {script_name}")
        return False

    try:
        subprocess.run(["python3", script_path], check=True)
        print(f"[SUCCESS] Ran: {script_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[FAIL] Error while running {script_name}: {e}")
        return False

if __name__ == "__main__":
    print("\n[INFO] WorldBuilder Orchestration Starting...\n")

    for script in script_order:
        if not run_script(script):
            print(f"[HALTED] Orchestration failed on: {script}")
            exit(1)

    print("\n[✔] AI taking over. MindGate successfully engaged.\n")

