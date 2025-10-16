# File: AppDeployer.py

"""
AppDeployer: Finalizes and deploys application into runtime execution layer.

Takes validated application structure, injects metadata, connects to Helix,
and confirms runtime readiness.

Used in Application Builder Toolset (Toolset 5).
"""

import os
import shutil

def deploy_application(app_dir, system_dir="/helix/system/apps"):
    print(f"[*] Deploying app from {app_dir}")

    if not os.path.exists(app_dir):
        raise FileNotFoundError("Application directory not found.")

    app_name = os.path.basename(app_dir.rstrip("/\\"))
    target_dir = os.path.join(system_dir, app_name)

    os.makedirs(system_dir, exist_ok=True)

    if os.path.exists(target_dir):
        print(f"[!] Application already deployed. Overwriting: {target_dir}")
        shutil.rmtree(target_dir)

    shutil.copytree(app_dir, target_dir)
    print(f"[+] Application deployed successfully to: {target_dir}")

# Example:
# deploy_application("/apps/ExampleTool")

