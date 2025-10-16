# CommandInterfaceRegenerator.py

import re
import os
from docx import Document

def parse_interface_doc(doc_path):
    doc = Document(doc_path)
    tool_data = {}
    current_tool = None

    for para in doc.paragraphs:
        text = para.text.strip()

        if text.startswith("Tool:"):
            current_tool = text.split("Tool:")[1].strip()
            tool_data[current_tool] = {"buttons": {}, "flags": [], "connections": {}}

        elif re.match(r"^\d+\.", text):  # Button line: "1. Diagnose"
            num, label = text.split('.', 1)
            tool_data[current_tool]["buttons"][int(num.strip())] = label.strip()

        elif text.lower().startswith("flags:"):
            continue  # skip

        elif text.startswith("--"):
            tool_data[current_tool]["flags"].append(text.strip())

        elif "→" in text:
            num, func = map(str.strip, text.split("→", 1))
            tool_data[current_tool]["connections"][int(num)] = func

    return tool_data


def inject_interface(tool_name, tool_data, base_dir="ToolSet/"):
    path = os.path.join(base_dir, f"{tool_name}.qtl")
    if not os.path.exists(path):
        print(f"Tool script {path} not found.")
        return

    with open(path, 'r') as f:
        original = f.read()

    # Strip old interface block
    cleaned = re.sub(r"# BEGIN_INTERFACE(.*?)# END_INTERFACE", "", original, flags=re.DOTALL)

    new_block = ["# BEGIN_INTERFACE"]
    new_block.append(f"# Auto-generated interface for {tool_name}")

    # Generate button menu
    new_block.append("menu_options = {")
    for num, label in tool_data["buttons"].items():
        new_block.append(f"    {num}: '{label}',")
    new_block.append("}")
    new_block.append("")

    # Add flag handler
    new_block.append("flags = [")
    for flag in tool_data["flags"]:
        new_block.append(f"    '{flag}',")
    new_block.append("]")
    new_block.append("")

    # Add connection routing
    new_block.append("def run_selection(selection):")
    for num, call in tool_data["connections"].items():
        new_block.append(f"    if selection == {num}:")
        new_block.append(f"        {call}")
    new_block.append("    else:")
    new_block.append("        print('Invalid selection')")
    new_block.append("# END_INTERFACE")

    full_output = cleaned.strip() + "\n\n" + "\n".join(new_block)

    with open(path, 'w') as f:
        f.write(full_output)

    print(f"Updated interface for {tool_name}.")


def main():
    config_path = "InterfaceLogic.docx"
    base_dir = "ToolSet/"
    toolset = parse_interface_doc(config_path)
    
    for tool_name, data in toolset.items():
        inject_interface(tool_name, data, base_dir)

if __name__ == "__main__":
    main()

