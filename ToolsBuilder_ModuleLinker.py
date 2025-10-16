# ToolsBuilder_ModuleLinker.py
# Links core logic modules into an application scaffold using dependency order and tool graph.

import os
import json

class ModuleLinker:
    def __init__(self, link_config_path):
        self.link_config_path = link_config_path
        self.link_graph = {}

    def load_graph(self):
        with open(self.link_config_path, 'r') as f:
            self.link_graph = json.load(f)

    def link_modules(self, output_path):
        linked_code = ""
        for module in self.link_graph.get("order", []):
            path = self.link_graph["modules"].get(module)
            if path and os.path.exists(path):
                with open(path, 'r') as f:
                    linked_code += f"\n# Begin {module}\n" + f.read() + f"\n# End {module}\n"
        with open(output_path, 'w') as out:
            out.write(linked_code)
        print("[Module Linking Completed]")

if __name__ == "__main__":
    linker = ModuleLinker("module_link_config.json")
    linker.load_graph()
    linker.link_modules("linked_output.py")

