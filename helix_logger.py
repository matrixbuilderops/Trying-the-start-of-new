
from Tools.Configurations.validator_hooks import qtl_validate_helix_logger, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_path import current_timestamp

def start_logging():
    timestamp = current_timestamp()
    qtl = qtl_validate_helix_logger(requester="helix_logger", command="start_log", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)
    # Logging logic here
    print("Helix logging started — QTL protected.")
