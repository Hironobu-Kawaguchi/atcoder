mod solver {
    #![allow(dead_code)]

    include!("agent_jump_tree_v11_thick_delta.rs");
    include!("agent_jump_tree_v12_beam_delta_common.rs");
    include!("agent_jump_tree_v14_fast_k16_common.rs");
    include!("agent_jump_tree_v15_segment_batch_common.rs");
}

fn main() {
    solver::run_v15_segment_batch();
}
