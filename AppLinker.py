# File: AppLinker.py

"""
AppLinker: Wires together application modules, handlers, and runtime endpoints.
Used in Application Builder Toolset (Toolset 5).

Takes compiled interface specs, handler maps, and wiring configs,
and generates runtime bindings for Helix or connected toolsets.
"""

import os

def link_application_components(app_dir):
    interface_file = os.path.join(app_dir, "hooks", "app_hook.qtl")
    handler_dir = os.path.join(app_dir, "handlers")
    output_file = os.path.join(app_dir, "compiled", "link_map.qtl")

    if not os.path.exists(interface_file):
        raise FileNotFoundError("Interface hook file not found.")

    if not os.path.exists(handler_dir):
        raise FileNotFoundError("Handler directory missing.")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as out:
        out.write("# Application Link Map\n")
        out.write("BEGIN_LINK_TABLE\n\n")

        for handler in os.listdir(handler_dir):
            if handler.endswith(".py") or handler.endswith(".qtl"):
                handler_name = os.path.splitext(handler)[0]
                out.write(f"LINK {handler_name} => handlers/{handler}\n")

        out.write("\nEND_LINK_TABLE\n")

    print(f"[+] Application components linked: {output_file}")

# Example:
# link_application_components("/apps/ExampleTool")

