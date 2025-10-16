# QTL_ID: QTLConsistencyAudit_005
# Name: QTL Consistency Auditor
# Purpose: Scans project for naming drift and inconsistent declarations
# Hook: QTLHook::NameAudit
# Harness: TestHarness::DriftScan

def audit_qtl_ids(directory):
    import os
    seen_ids = {}
    conflicts = []

    for fname in os.listdir(directory):
        if not fname.endswith('.py'):
            continue
        with open(os.path.join(directory, fname), 'r') as f:
            for line in f:
                if line.startswith("# QTL_ID:"):
                    qtl_id = line.split(":")[1].strip()
                    if qtl_id in seen_ids:
                        conflicts.append((fname, seen_ids[qtl_id]))
                    seen_ids[qtl_id] = fname
    return conflicts

