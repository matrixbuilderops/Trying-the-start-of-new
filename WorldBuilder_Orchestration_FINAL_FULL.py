import os

SCRIPTS = [
    "CommandLogicImporter.py",
    "ChainLinkEngine_FIXED.py",
    "LogicCompiler.py",
    "QTLHookInjector.py",
    "MetaDataFormatter.py",
    "TestScriptGenerator.py",
    "ToolTemplateScanner.py",
    "FullMindGateEnable.py",
    "TalkToMindGate_ENHANCED.py"
]

def run_script(name):
    print(f"🔧 Executing: {name}")
    exit_code = os.system(f"python3 {name}")
    if exit_code != 0:
        print(f"❌ Error running {name} — Exit Code: {exit_code}")
    else:
        print(f"✅ {name} completed successfully.\n")

def main():
    print("\n📡 WorldBuilder Orchestration AI (Level 1000+)")
    print("==============================================\n")
    for script in SCRIPTS:
        run_script(script)
    print("🎯 Orchestration Complete: All systems triggered.")

if __name__ == "__main__":
    main()
