# https://atcoder.jp/contests/abc313/tasks/abc313_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    ans = max(ans, P[i]-P[0]+1)
print(ans)