# QTL_ID: QTLHealthMonitor_003
# Name: Health Monitor
# Purpose: Evaluates systemic health status of every tool file and flags broken hooks
# Hook: QTLHook::SystemCheck
# Harness: TestHarness::LiveVitals

import os

def monitor_health(directory):
    report = {}
    for fname in os.listdir(directory):
        if fname.endswith('.py'):
            with open(os.path.join(directory, fname), 'r') as file:
                content = file.read()
            if "def" not in content or "QTLHook" not in content:
                report[fname] = "❌ Incomplete"
            else:
                report[fname] = "✅ OK"
    return report

