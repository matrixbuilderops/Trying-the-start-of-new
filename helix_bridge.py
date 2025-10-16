
from Tools.Configurations.validator_hooks import qtl_validate_helix_bridge, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_path import current_timestamp

def bridge_signal():
    timestamp = current_timestamp()
    qtl = qtl_validate_helix_bridge(requester="helix_bridge", command="bridge_engage", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)
    # Original bridge logic preserved
    print("Helix bridge module active with QTL seal.")
