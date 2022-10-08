# https://atcoder.jp/contests/abc271/tasks/abc271_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]
for i in range(Q):
    s, t = map(int, input().split())
    print(A[s-1][t])
