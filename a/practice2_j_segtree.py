# https://atcoder.jp/contests/practice2/tasks/practice2_j
# https://github.com/not522/ac-library-python/blob/master/example/segtree_practice.py

import sys
sys.setrecursionlimit(10 ** 7)
from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

s = SegTree(max, -1, A)     # SegTree(op, e, v)

for qi in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:      # SegTree.set(pos, x)
        s.set(x - 1, y)
    elif t == 2:    # SegTree.prod(left, right)
        print(s.prod(x - 1, y))
    else:           # SegTree.max_right(left, f)
        print(s.max_right(x - 1, lambda v: v < y) + 1)
