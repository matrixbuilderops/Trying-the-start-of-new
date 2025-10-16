import os
import ast

TEST_OUTPUT_DIR = os.path.join("Tools", "TestHarness", "GeneratedTests")

def extract_definitions(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read(), filename=file_path)

    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return functions, classes

def generate_test_script(filename, functions, classes):
    base_name = os.path.splitext(os.path.basename(filename))[0]
    test_lines = [
        "import unittest",
        f"import {base_name}",
        "",
        f"class Test{base_name.capitalize()}(unittest.TestCase):"
    ]

    if not functions and not classes:
        test_lines.append("    pass")

    for func in functions:
        test_lines.extend([
            f"    def test_{func}(self):",
            f"        # TODO: Add test for {func}",
            f"        self.assertTrue(True)",
            ""
        ])

    for cls in classes:
        test_lines.extend([
            f"    def test_{cls}_instantiation(self):",
            f"        instance = {base_name}.{cls}()",
            f"        self.assertIsInstance(instance, {base_name}.{cls})",
            ""
        ])

    return "\n".join(test_lines)

def ensure_output_directory():
    if not os.path.exists(TEST_OUTPUT_DIR):
        os.makedirs(TEST_OUTPUT_DIR)

def run():
    ensure_output_directory()
    current_file = os.path.basename(__file__)
    for file in os.listdir("."):
        if file.endswith(".py") and file != current_file:
            functions, classes = extract_definitions(file)
            test_script = generate_test_script(file, functions, classes)
            test_filename = f"test_{os.path.splitext(file)[0]}.py"
            test_path = os.path.join(TEST_OUTPUT_DIR, test_filename)
            with open(test_path, "w") as test_file:
                test_file.write(test_script)
    print(f"[TestScriptGenerator] All test files written to {TEST_OUTPUT_DIR}")

if __name__ == "__main__":
    run()

