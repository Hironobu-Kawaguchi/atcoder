mod solver {
    #![allow(dead_code)]
    include!("agent_jump_tree_v11_thick_delta.rs");
    include!("agent_jump_tree_v12_beam_delta_common.rs");
}

fn main() {
    solver::run_v12::<16>();
}
