# Condenser — Structural and Logical Condensation Engine
# Minimizes redundant or unused code logic across QTL/Python scripts
# Focused on function simplification, def consolidation, and logical flattening

import os
import ast
import astor

class FunctionDeduplicator(ast.NodeTransformer):
    def __init__(self):
        self.known_funcs = {}

    def visit_FunctionDef(self, node):
        src = astor.to_source(node).strip()
        hash_key = hash(src)
        if hash_key in self.known_funcs:
            return None  # Drop duplicate function
        self.known_funcs[hash_key] = node.name
        return node

def condense_python_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()

        tree = ast.parse(source)
        deduplicator = FunctionDeduplicator()
        condensed_tree = deduplicator.visit(tree)
        ast.fix_missing_locations(condensed_tree)

        condensed_code = astor.to_source(condensed_tree)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(condensed_code)

    except Exception as e:
        print(f"[!] Failed to condense {file_path}: {e}")

def walk_and_condense(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.qtl'):
                condense_python_code(os.path.join(root, file))

if __name__ == "__main__":
    walk_and_condense(".")

