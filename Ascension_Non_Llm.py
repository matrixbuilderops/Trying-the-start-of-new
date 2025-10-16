"""
Ascension — QTL-Bound Clean-Room Tool (Non-LLM Version)
"""
from Tools.Configurations.validator_hooks import qtl_validate_ascension, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_cli import parse_cli_args, cli_menu
from Tools.Configurations.worldbuilder_runner import rerun_godtree_outputs, rerun_analyzer_outputs
from Tools.Configurations.worldbuilder_path import ensure_output_structure, current_timestamp
from Tools.Configurations.worldbuilder_snapshot import record_tool_snapshot
from Tools.Configurations.helix_controller import (
    run_helix_analysis,
    run_helix_fix,
    run_ai_model_linking,
    create_backup,
    restore_backup_by_timestamp,
    organize_system_structure
)
from Tools.Configurations.worldbuilder_diagnostics import generate_diagnostic_report
from Tools.Configurations.worldbuilder_ingest import ingest_files_from_folder

def main() -> None:
    tool_name = "ascension"
    timestamp = current_timestamp()

    # QTL validation
    qtl = qtl_validate_ascension(requester="user", command="cli_entry", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)

    ensure_output_structure(tool_name=tool_name, timestamp=timestamp)
    args = parse_cli_args(tool_name)

    # CLI Flags
    if args.run_all:
        rerun_godtree_outputs()
        rerun_analyzer_outputs()
        ingest_files_from_folder(timestamp)
        run_ai_model_linking(timestamp)
        run_helix_analysis(timestamp)
        run_helix_fix(timestamp)
        organize_system_structure(timestamp)
        create_backup(tool_name, timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.rerun_godtree:
        rerun_godtree_outputs()
        return

    if args.rerun_analyzer:
        rerun_analyzer_outputs()
        return

    if args.diagnose:
        generate_diagnostic_report(tool_name, timestamp)
        return

    if args.create_backup:
        create_backup(tool_name, timestamp)
        return

    if args.restore_backup:
        restore_backup_by_timestamp(tool_name)
        return

    # Menu CLI
    while True:
        print("\n[Ascension CLI Menu]")
        print("[1] Run Everything")
        print("[2] Rerun GodTree")
        print("[3] Rerun Analyzer")
        print("[4] Ingest Files from Folder")
        print("[5] AI Model Linking")
        print("[6] Helix Analyze")
        print("[7] Helix Fix")
        print("[8] System Organization")
        print("[9] Create Backup")
        print("[10] Restore Backup")
        print("[11] Diagnostics Only")
        print("[12] Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            rerun_godtree_outputs()
            rerun_analyzer_outputs()
            ingest_files_from_folder(timestamp)
            run_ai_model_linking(timestamp)
            run_helix_analysis(timestamp)
            run_helix_fix(timestamp)
            organize_system_structure(timestamp)
            create_backup(tool_name, timestamp)
            record_tool_snapshot(tool_name, timestamp)
        elif choice == "2":
            rerun_godtree_outputs()
        elif choice == "3":
            rerun_analyzer_outputs()
        elif choice == "4":
            ingest_files_from_folder(timestamp)
        elif choice == "5":
            run_ai_model_linking(timestamp)
        elif choice == "6":
            run_helix_analysis(timestamp)
        elif choice == "7":
            run_helix_fix(timestamp)
        elif choice == "8":
            organize_system_structure(timestamp)
        elif choice == "9":
            create_backup(tool_name, timestamp)
        elif choice == "10":
            restore_backup_by_timestamp(tool_name)
        elif choice == "11":
            generate_diagnostic_report(tool_name, timestamp)
        elif choice == "12":
            print("Exiting Ascension.")
            break
        else:
            print("Invalid option. Please select from 1 to 12.")

if __name__ == "__main__":
    main()

