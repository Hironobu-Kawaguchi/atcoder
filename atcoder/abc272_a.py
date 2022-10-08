# https://atcoder.jp/contests/abc271/tasks/abc272_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
ans = 0
for i in range(N):
    ans += A[i]
print(ans)
