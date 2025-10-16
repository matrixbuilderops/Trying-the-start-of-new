
from Tools.Configurations.validator_hooks import qtl_validate_analyzer, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_cli import parse_cli_args
from Tools.Configurations.worldbuilder_path import ensure_output_structure, current_timestamp
from Tools.Configurations.worldbuilder_snapshot import record_tool_snapshot
from Tools.Configurations.helix_controller import run_helix_analysis
from Tools.Configurations.worldbuilder_diagnostics import generate_diagnostic_report, summarize_analyzer_findings

def run_analyzer_outputs(tool_name: str, timestamp: str) -> None:
    print("[Analyzer] Launching Helix-Powered Analysis")
    run_helix_analysis(tool_name=tool_name, timestamp=timestamp)
    print("[Analyzer] Output completed")

def run_analyzer_diagnostics(tool_name: str, timestamp: str) -> None:
    print("[Analyzer] Running Diagnostics")
    generate_diagnostic_report(tool_name, timestamp)
    summarize_analyzer_findings(timestamp=timestamp)

def main() -> None:
    tool_name = "analyzer"
    timestamp = current_timestamp()

    qtl = qtl_validate_analyzer(requester="user", command="cli_entry", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)

    ensure_output_structure(tool_name=tool_name, timestamp=timestamp)
    args = parse_cli_args(tool_name)

    if args.run or args.helix:
        run_analyzer_outputs(tool_name, timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.diagnose:
        run_analyzer_diagnostics(tool_name, timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    while True:
        print("\n[Analyzer CLI Menu]")
        print("[1] Run Tool (Helix-powered)")
        print("[2] Run Diagnostics")
        print("[3] Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            run_analyzer_outputs(tool_name, timestamp)
            record_tool_snapshot(tool_name, timestamp)
        elif choice == "2":
            run_analyzer_diagnostics(tool_name, timestamp)
            record_tool_snapshot(tool_name, timestamp)
        elif choice == "3":
            print("Exiting Analyzer.")
            break
        else:
            print("Invalid option. Please select 1 to 3.")

if __name__ == "__main__":
    main()
