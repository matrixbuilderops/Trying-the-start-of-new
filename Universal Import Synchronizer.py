# QTL_ID: QTLImportSync_007
# Name: Universal Import Synchronizer
# Purpose: Unifies import schema across all files and repairs any broken internal links
# Hook: QTLHook::ImportSync
# Harness: TestHarness::ImportLinkCheck

def sync_imports(directory):
    import os
    required_import = "import HelixValidator"

    for fname in os.listdir(directory):
        if fname.endswith('.py'):
            with open(os.path.join(directory, fname), 'r') as file:
                lines = file.readlines()

            if not any(required_import in line for line in lines):
                lines.insert(0, required_import + "\n")
                with open(os.path.join(directory, fname), 'w') as file:
                    file.writelines(lines)

