# https://atcoder.jp/contests/abc313/tasks/abc313_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))
l = sum(A) // N
r = l + 1
# print(l, r, file=sys.stderr)
add, sub = 0, 0
for i in range(N):
    if A[i] < l:
        add += l - A[i]
    elif A[i] > r:
        sub += A[i] - r
print(max(add, sub))
