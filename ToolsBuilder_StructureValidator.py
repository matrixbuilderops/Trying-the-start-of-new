# ToolsBuilder_StructureValidator.py
# Validates that the directory and file hierarchy of a toolset matches expected standards.

import os

class StructureValidator:
    def __init__(self, base_path):
        self.base_path = base_path
        self.required_structure = {
            "Applications": ["InterfaceCompiler.py", "AppValidator.py"],
            "Scripts": ["AppDeployer.py", "AppLinker.py"],
            "Meta": ["AppMetaInjector.py"],
        }

    def validate(self):
        results = {}
        for folder, files in self.required_structure.items():
            folder_path = os.path.join(self.base_path, folder)
            folder_exists = os.path.isdir(folder_path)
            results[folder] = folder_exists and all(
                os.path.isfile(os.path.join(folder_path, f)) for f in files
            )
        return results

if __name__ == "__main__":
    validator = StructureValidator("/path/to/Toolset4")
    print(validator.validate())

