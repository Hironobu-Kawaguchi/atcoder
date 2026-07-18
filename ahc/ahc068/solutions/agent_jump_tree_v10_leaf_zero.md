# jump_tree_v10_leaf_zero

`agent_jump_tree_v10_leaf.rs`に`agent_jump_tree_v10_zero.rs`のゼロ壁専用・固定作業量
C-R-C早期分岐を統合した比較候補。

- 壁あり: `leaf`候補と静的同等。
- 壁0本: `zero`候補と同一ロジック。leaf探索は同時実行しない。
- 最終full replayとtree/jump安全フォールバックを維持。

## 静的確認

- `mesh_candidate`以降は`agent_jump_tree_v10_leaf.rs`と差分なし。
- `rustfmt --check`: 成功
- `rustc --edition 2021 -O -D warnings`: 成功
- ソルバの入力実行は未実施。
