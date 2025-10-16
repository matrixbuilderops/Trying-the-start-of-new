# QTL_ID: QTLFlagCheck_004
# Name: Command Flag Integrity Checker
# Purpose: Validates that each tool’s command-line flags correspond to implemented features
# Hook: QTLHook::FlagScan
# Harness: TestHarness::CommandParserCheck

def check_flags(tool_code):
    required_flags = ["--run", "--dry-run", "--help"]
    found = [flag for flag in required_flags if flag in tool_code]
    missing = list(set(required_flags) - set(found))
    return {"found": found, "missing": missing}

