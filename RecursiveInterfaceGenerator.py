# RecursiveInterfaceGenerator.py

"""
Reads a Word document describing tool front-ends, flags, and options.
Builds and injects those interfaces recursively into the correct tool layer.
Used for generating interface shells, command bindings, and Helix forward hooks.
"""

import os
import json
import docx

def parse_interface_doc(doc_path):
    doc = docx.Document(doc_path)
    structure = {}
    current_tool = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text: continue
        if text.lower().startswith("tool:"):
            current_tool = text.split(":", 1)[1].strip()
            structure[current_tool] = {"flags": [], "options": []}
        elif text.lower().startswith("flag:"):
            structure[current_tool]["flags"].append(text.split(":", 1)[1].strip())
        elif text.lower().startswith("option:"):
            structure[current_tool]["options"].append(text.split(":", 1)[1].strip())

    return structure

def build_interface_bindings(interface_data, output_dir="Toolset_Interfaces"):
    os.makedirs(output_dir, exist_ok=True)
    for tool, data in interface_data.items():
        out_path = os.path.join(output_dir, f"{tool}_interface.json")
        with open(out_path, 'w') as f:
            json.dump({
                "tool": tool,
                "flags": data["flags"],
                "options": data["options"],
                "recursive_hooks": True,
                "helix_sync": True
            }, f, indent=4)
        print(f"[✔] Generated interface config for {tool}")

def generate_from_doc(doc_path):
    parsed = parse_interface_doc(doc_path)
    build_interface_bindings(parsed)

if __name__ == "__main__":
    # Example usage — replace with actual .docx interface spec
    generate_from_doc("InterfaceSpec.docx")

