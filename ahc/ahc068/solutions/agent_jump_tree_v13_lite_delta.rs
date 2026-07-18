mod solver {
    #![allow(dead_code)]
    include!("agent_jump_tree_v11_thick_safe.rs");
    include!("agent_jump_tree_v13_lite_delta_common.rs");
}

fn main() {
    solver::run_lite_delta_v13::<false>();
}
