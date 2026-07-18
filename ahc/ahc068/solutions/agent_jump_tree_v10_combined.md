# jump_tree_v10_combined

`agent_jump_tree_v10_straight.rs`と`agent_jump_tree_v10_zero.rs`の統合候補。

- 壁あり: `straight`候補をそのまま実行する。
- 壁0本: `zero`候補の固定作業量C-R-Cルータへ早期分岐し、`straight`側の
  探索・木候補は同時生成しない。

ゼロ壁ビームは幅200、深さ14、1ライン240,000展開、全体14,400,000展開。
時間を参照せず、未完ラインは隣接交換で完成させる。最終full replayに失敗した
場合だけ安全なtree/jump補完へ戻る。

## 静的確認

- `mesh_candidate`以降は`agent_jump_tree_v10_straight.rs`と差分なし。
- ゼロ壁関数は`agent_jump_tree_v10_zero.rs`と同一ロジック。
- `rustfmt --check`: 成功
- `rustc --edition 2021 -O -D warnings`: 成功
- ソルバの入力実行は未実施。

ゼロ壁側は実行時間を加算しない排他的分岐であり、同一ケースでstraight候補との
短い方を選ぶ単調ガードではない。公式ケース評価時には、特に固定14.4M展開の
2秒余裕を確認する。
