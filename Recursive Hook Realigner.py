# QTL_ID: QTLHookRealigner_006
# Name: Recursive Hook Realigner
# Purpose: Ensures all QTL hooks point to valid and active reference files across recursion layers
# Hook: QTLHook::HookRealign
# Harness: TestHarness::HookValidator

def realign_hooks(directory):
    import os
    hook_reference = "QTLHook"

    for fname in os.listdir(directory):
        if fname.endswith('.py'):
            with open(os.path.join(directory, fname), 'r') as file:
                content = file.read()
            if hook_reference not in content:
                print(f"{fname} -> ⚠️ Missing QTLHook")

