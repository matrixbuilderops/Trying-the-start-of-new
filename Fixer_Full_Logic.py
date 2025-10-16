"""
Fixer — QTL-Bound Clean-Room Tool with Full Logic and Dual CLI
"""
from Tools.Configurations.validator_hooks import qtl_validate_fixer, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_cli import parse_cli_args, cli_menu
from Tools.Configurations.worldbuilder_runner import run_helix_fixer_pass
from Tools.Configurations.worldbuilder_diagnostics import generate_diagnostic_report, summarize_fixer_findings
from Tools.Configurations.worldbuilder_path import ensure_output_structure, current_timestamp
from Tools.Configurations.worldbuilder_snapshot import record_tool_snapshot
from Tools.Configurations.helix_controller import (
    run_fixer_analysis,
    run_fixer_structure_organizer,
    run_ai_model_detection,
    run_ai_model_linking,
    delete_quarantined,
    delete_unused,
    create_backup,
    restore_backup_by_timestamp
)

def main() -> None:
    tool_name = "fixer"
    timestamp = current_timestamp()

    # QTL check
    qtl = qtl_validate_fixer(requester="user", command="cli_entry", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)

    ensure_output_structure(tool_name=tool_name, timestamp=timestamp)
    args = parse_cli_args(tool_name)

    # CLI Flag Routes
    if args.run_all:
        run_fixer_analysis(timestamp)
        run_ai_model_linking(timestamp)
        run_helix_fixer_pass(tool_name, timestamp)
        run_fixer_structure_organizer(timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.diagnose:
        generate_diagnostic_report(tool_name, timestamp)
        summarize_fixer_findings(timestamp=timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.helix_analyze:
        run_fixer_analysis(timestamp)
        return

    if args.helix_fix:
        run_helix_fixer_pass(tool_name, timestamp)
        return

    if args.structure:
        run_fixer_structure_organizer(timestamp)
        return

    if args.detect_models:
        run_ai_model_detection(timestamp)
        return

    if args.wire_models:
        run_ai_model_linking(timestamp)
        return

    if args.delete_unused:
        delete_unused(timestamp)
        return

    if args.delete_quarantine:
        delete_quarantined(timestamp)
        return

    if args.create_backup:
        create_backup(tool_name, timestamp)
        return

    if args.restore_backup:
        restore_backup_by_timestamp(tool_name)
        return

    # Menu CLI
    while True:
        print("\n[Fixer CLI Menu]")
        print("[1] Helix Analyze")
        print("[2] Helix Fix")
        print("[3] Detect AI Models")
        print("[4] Wire AI Models")
        print("[5] Delete Unused Files")
        print("[6] Delete Quarantine Files")
        print("[7] Create Backup")
        print("[8] Restore Backup")
        print("[9] System Organization")
        print("[10] Diagnostics Only")
        print("[11] Run Everything")
        print("[12] Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            run_fixer_analysis(timestamp)
        elif choice == "2":
            run_helix_fixer_pass(tool_name, timestamp)
        elif choice == "3":
            run_ai_model_detection(timestamp)
        elif choice == "4":
            run_ai_model_linking(timestamp)
        elif choice == "5":
            delete_unused(timestamp)
        elif choice == "6":
            delete_quarantined(timestamp)
        elif choice == "7":
            create_backup(tool_name, timestamp)
        elif choice == "8":
            restore_backup_by_timestamp(tool_name)
        elif choice == "9":
            run_fixer_structure_organizer(timestamp)
        elif choice == "10":
            generate_diagnostic_report(tool_name, timestamp)
            summarize_fixer_findings(timestamp=timestamp)
        elif choice == "11":
            run_fixer_analysis(timestamp)
            run_ai_model_linking(timestamp)
            run_helix_fixer_pass(tool_name, timestamp)
            run_fixer_structure_organizer(timestamp)
        elif choice == "12":
            print("Exiting Fixer.")
            break
        else:
            print("Invalid option. Please select from 1 to 12.")

if __name__ == "__main__":
    main()

