# ModelRefactorer.py
# Takes existing 2-part models and merges/upgrades them into single-file QTL

from pathlib import Path

def merge_model_parts(part1_path: str, part2_path: str, output_path: str, new_model_name: str):
    with open(part1_path, 'r') as f1, open(part2_path, 'r') as f2:
        part1 = f1.read()
        part2 = f2.read()

    merged = (
        "# QTLHook\n"
        f"ModelName: {new_model_name}\n"
        "# Part 1\n" + part1 + "\n"
        "# Part 2\n" + part2 + "\n"
        "# Merged by ModelRefactorer\n"
    )

    output_file = Path(output_path) / f"{new_model_name}.qtl"
    with open(output_file, 'w') as f:
        f.write(merged)

    print(f"Merged model written to: {output_file}")

# Example usage
# merge_model_parts("OldModel/Model_A_Part1.qtl", "OldModel/Model_A_Part2.qtl", "NewModel/", "Model_A_Refactored")

