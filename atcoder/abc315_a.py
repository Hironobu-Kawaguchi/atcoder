# https://atcoder.jp/contests/abc315/tasks/abc315_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

l = ['a', 'e', 'i', 'o', 'u']
S = input()

ans = ""
for s in S:
    if s not in l:
        ans += s
print(ans)
