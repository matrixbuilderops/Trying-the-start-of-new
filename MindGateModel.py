# MindGateModel.py

import subprocess
import os

def enable_mindgate():
    mindgate_path = os.path.join(
        os.getcwd(),
        "Tools",
        "Helix",
        "Backend",
        "Models",
        "MindGate.qtl"
    )

    if not os.path.isfile(mindgate_path):
        print(f"[FATAL] MindGate.qtl not found at: {mindgate_path}")
        raise SystemExit(1)

    try:
        result = subprocess.run(
            ["qtl", mindgate_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("[MindGate] Execution output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("[MindGate ERROR]", e.stderr)
        raise SystemExit(1)

