# jump_tree_v15 short-line PDB

V14 Fast K16 is retained unchanged as the mandatory baseline. V15 adds an
optional semantics-preserving peephole pass over the resulting operation
sequence.

## Safe replacement domain

A candidate window must consist entirely of consecutive thin operations on
one physical line (`H` with height 1, or `V` with width 1). Its complete
affected span must have length at most 8 and be wall-free. Therefore the
window is a closed permutation of at most eight cells and has no effect
outside that span.

For each required span length, a BFS pattern database enumerates all equal
adjacent block exchanges, including adjacent swaps. The original window's net
permutation is replaced only when the BFS path is strictly shorter. Dynamic
programming chooses a non-overlapping set of replacements with minimum total
operation count. Each replacement has exactly the same permutation as its
source window, so it remains equivalent in every surrounding board context.

## Guards and budget

- Windows are bounded to 24 source operations; this limits work but does not
  affect correctness.
- Postprocessing starts only if V14 returns before 1.780 seconds.
- PDB construction and window scanning abort at 1.840 seconds.
- Any abort returns the original V14 output.
- A candidate is accepted only when it is globally shorter and a full replay
  proves legality and completion.

## Validation status

Only formatting and optimized compilation are performed in this implementation
turn. No solver input is executed, in accordance with the contest's generative
AI usage rule.
