"""
Ascension — Full Logic, QTL-Enabled, Helix-Integrated, CLI + Flag Matrix
"""
from Tools.Configurations.validator_hooks import qtl_validate_ascension, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_cli import parse_cli_args, cli_menu
from Tools.Configurations.worldbuilder_runner import run_helix_ascension_pass
from Tools.Configurations.worldbuilder_diagnostics import generate_diagnostic_report
from Tools.Configurations.worldbuilder_path import ensure_output_structure, current_timestamp
from Tools.Configurations.worldbuilder_snapshot import record_tool_snapshot
from Tools.Configurations.helix_controller import (
    run_ascension_merge,
    run_ascension_recompile,
    run_ai_model_role_reassignment,
    scan_input_files,
    trigger_llm_conversation,
    run_safe_mode_simulation,
    dry_run_all_actions,
    create_backup,
    restore_backup_by_timestamp,
    run_full_ascension_stack
)

def main() -> None:
    tool_name = "ascension"
    timestamp = current_timestamp()

    # QTL Validation
    qtl = qtl_validate_ascension(requester="user", command="cli_entry", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)

    ensure_output_structure(tool_name=tool_name, timestamp=timestamp)
    args = parse_cli_args(tool_name)

    # CLI Flag Routes
    if args.run_all:
        run_full_ascension_stack(timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.merge:
        run_ascension_merge(timestamp)
        return

    if args.recompile:
        run_ascension_recompile(timestamp)
        return

    if args.diagnose:
        generate_diagnostic_report(tool_name, timestamp)
        record_tool_snapshot(tool_name, timestamp)
        return

    if args.role_reassign:
        run_ai_model_role_reassignment(timestamp)
        return

    if args.ingest:
        scan_input_files(timestamp)
        return

    if args.talk:
        trigger_llm_conversation()
        return

    if args.safemode:
        run_safe_mode_simulation(timestamp)
        return

    if args.dryrun:
        dry_run_all_actions(timestamp)
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
        print("[1] Merge Ascension Structures")
        print("[2] Recompile Outputs")
        print("[3] Reassign AI Model Roles")
        print("[4] Ingest Files from Input Folder")
        print("[5] Initiate LLM Conversation")
        print("[6] Enable Safe Mode")
        print("[7] Execute Dry Run")
        print("[8] Create Backup")
        print("[9] Restore from Backup")
        print("[10] Diagnostics")
        print("[11] Run Everything")
        print("[12] Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            run_ascension_merge(timestamp)
        elif choice == "2":
            run_ascension_recompile(timestamp)
        elif choice == "3":
            run_ai_model_role_reassignment(timestamp)
        elif choice == "4":
            scan_input_files(timestamp)
        elif choice == "5":
            trigger_llm_conversation()
        elif choice == "6":
            run_safe_mode_simulation(timestamp)
        elif choice == "7":
            dry_run_all_actions(timestamp)
        elif choice == "8":
            create_backup(tool_name, timestamp)
        elif choice == "9":
            restore_backup_by_timestamp(tool_name)
        elif choice == "10":
            generate_diagnostic_report(tool_name, timestamp)
        elif choice == "11":
            run_full_ascension_stack(timestamp)
        elif choice == "12":
            print("Exiting Ascension.")
            break
        else:
            print("Invalid option. Please select from 1 to 12.")

if __name__ == "__main__":
    main()

