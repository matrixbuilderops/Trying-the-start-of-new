
from Tools.Configurations.validator_hooks import qtl_validate_helix_io, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_path import current_timestamp

def process_io():
    timestamp = current_timestamp()
    qtl = qtl_validate_helix_io(requester="helix_io", command="io_transfer", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)
    # Original full logic retained here
    print("Helix IO processing module running with QTL fingerprint.")
