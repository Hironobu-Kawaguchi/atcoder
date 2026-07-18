mod solver {
    #![allow(dead_code)]
    include!("agent_jump_tree_v11_thick_delta.rs");
    include!("agent_jump_tree_v12_beam_delta_common.rs");
    include!("agent_jump_tree_v14_k8_deadline_common.rs");
}

fn main() {
    solver::run_k8_deadline_v14();
}
