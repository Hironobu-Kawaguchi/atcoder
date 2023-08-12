# https://atcoder.jp/contests/abc310/tasks/abc310_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()

zero, one = 0, 0
ans = 0
for s in S:
    if s=='0':
        zero, one = 1, zero + one
    else:
        zero, one = one, zero + 1
    ans += one
print(ans)
