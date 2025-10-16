
from Tools.Configurations.validator_hooks import qtl_validate_helix_comm, qtl_exit_if_blocked
from Tools.Configurations.worldbuilder_path import current_timestamp

def comm_init():
    timestamp = current_timestamp()
    qtl = qtl_validate_helix_comm(requester="helix_comm", command="init_comm", timestamp=timestamp)
    qtl_exit_if_blocked(qtl)
    # Communication logic complete
    print("Helix communications initialized — QTL-locked.")
