# ToolsBuilder_InterfaceRegistry.py
# Registers and validates interface definitions for Toolset4 applications.

import os
import json

class InterfaceRegistry:
    def __init__(self, registry_path):
        self.registry_path = registry_path
        self.registry = {}

    def register_interface(self, tool_name, interface_schema):
        self.registry[tool_name] = interface_schema

    def save(self):
        with open(self.registry_path, 'w') as f:
            json.dump(self.registry, f, indent=2)

    def validate_schema_keys(self, required_keys):
        invalid = []
        for tool, schema in self.registry.items():
            for key in required_keys:
                if key not in schema:
                    invalid.append((tool, key))
        return invalid

if __name__ == "__main__":
    reg = InterfaceRegistry("interface_registry.json")
    reg.register_interface("AppDeployer", {"input": "str", "output": "bool", "config": "dict"})
    reg.save()
    missing_keys = reg.validate_schema_keys(["input", "output", "config"])
    print("[Schema Validation]", "OK" if not missing_keys else f"Missing: {missing_keys}")

