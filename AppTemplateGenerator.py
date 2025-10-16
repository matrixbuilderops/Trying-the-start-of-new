# File: AppTemplateGenerator.py

"""
AppTemplateGenerator: Core utility for scaffolding new applications
within the Application Builder Toolset (Toolset 5).

Outputs a fully structured app directory with:
- Metadata stub
- Hook framework
- Logical command scaffolds
- Import anchors
- Placeholder test routines
"""

import os
from datetime import datetime

TEMPLATE_STRUCTURE = {
    "core": ["main.py", "logic.py"],
    "interfaces": ["cli_interface.py", "gui_stub.py"],
    "hooks": ["app_hook.qtl"],
    "metadata": ["app_meta.qtl"],
    "tests": ["test_app.py"]
}

def create_app_template(app_name, base_dir="Applications"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    app_folder = os.path.join(base_dir, f"{app_name}_{timestamp}")

    if not os.path.exists(app_folder):
        os.makedirs(app_folder)

    for subdir, files in TEMPLATE_STRUCTURE.items():
        subpath = os.path.join(app_folder, subdir)
        os.makedirs(subpath, exist_ok=True)

        for f in files:
            file_path = os.path.join(subpath, f)
            with open(file_path, "w") as file:
                file.write(f"# {f} – placeholder for {app_name} application\n")

    # Root README for visibility
    readme_path = os.path.join(app_folder, "README.md")
    with open(readme_path, "w") as file:
        file.write(f"# {app_name} Application Template\nGenerated on {timestamp}\n\n")

    print(f"[✔] Application template created at: {app_folder}")
    return app_folder

# Example Usage:
# create_app_template("InventoryManager")

