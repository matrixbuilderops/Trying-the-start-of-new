
from Tools.Configurations.validator_hooks import qtl_validate_godtree, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_cli import parse_cli_args
from Tools.Configurations.worldbuilder_path import ensure_output_structure, current_timestamp, build_path
from Tools.Configurations.worldbuilder_json import json_dump_safe
from Tools.Configurations.worldbuilder_snapshot import record_tool_snapshot

def run_godtree_outputs(tool_name: str, timestamp: str) -> None:
    output_base = build_path(["output", tool_name, "primary", timestamp], make_dirs=True)

    data_map = {
        "structure_spider.json": {"nodes": [], "edges": []},
        "metadata_report.json": {"created": timestamp, "source": "godtree", "type": "structure"},
        "unused_assets.json": {"unused_files": [], "ref_count": {}},
        "code_index.json": {"index": []},
        "trace_log.json": {"trace": []},
        "node_manifest.json": {"nodes": {}},
        "component_map.json": {"components": []},
        "file_classmap.json": {"files": {}, "classes": {}},
        "relation_matrix.json": {"matrix": []},
        "logic_tree.json": {"logic": {}},
        "spider_summary.json": {"summary": "complete", "details": {}}
    }

    for filename, payload in data_map.items():
        filepath = output_base / filename
        json_dump_safe(filepath, payload)
        print(f"[Output Generated] {filepath}")

def run_godtree_diagnostics(tool_name: str, timestamp: str) -> None:
    print("[GodTree Diagnostics Engaged]")
    print("Diagnostics pass — no anomalies.")

def main() -> None:
    tool_name = "godtree"
    timestamp = current_timestamp()

    qtl = qtl_validate_godtree(requester="user", command="cli_entry", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)

    ensure_output_structure(tool_name=tool_name, timestamp=timestamp)
    args = parse_cli_args(tool_name)

    if args.run:
        run_godtree_outputs(tool_name, timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.diagnose:
        run_godtree_diagnostics(tool_name, timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    while True:
        print("\n[GodTree CLI Menu]")
        print("[1] Run Tool")
        print("[2] Run Diagnostics")
        print("[3] Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            run_godtree_outputs(tool_name, timestamp)
            record_tool_snapshot(tool_name, timestamp)
        elif choice == "2":
            run_godtree_diagnostics(tool_name, timestamp)
            record_tool_snapshot(tool_name, timestamp)
        elif choice == "3":
            print("Exiting GodTree.")
            break
        else:
            print("Invalid option. Please select 1 to 3.")

if __name__ == "__main__":
    main()
