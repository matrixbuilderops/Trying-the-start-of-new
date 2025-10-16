
from Tools.Configurations.validator_hooks import qtl_validate_helix_core, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_path import current_timestamp

def run_core():
    timestamp = current_timestamp()
    qtl = qtl_validate_helix_core(requester="helix_core", command="start_core", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)
    # Original full logic retained here
    print("Helix core operational with full QTL binding.")
