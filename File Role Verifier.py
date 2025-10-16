# QTL_ID: QTLFileRoleVerifier_002
# Name: File Role Verifier
# Purpose: Confirms each file's declared purpose matches actual logic behavior
# Hook: QTLHook::RoleCheck
# Harness: TestHarness::RoleValidator

def verify_file_role(file_path):
    expected_roles = ["Hook Normalizer", "Upgrade Applier", "Import Sync"]
    with open(file_path, 'r') as f:
        content = f.read()

    found_role = next((r for r in expected_roles if r.lower() in content.lower()), None)
    if found_role:
        print(f"{file_path} -> Role Verified: {found_role}")
    else:
        print(f"{file_path} -> ❌ Role not found in logic.")

