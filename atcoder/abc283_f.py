# https://atcoder.jp/contests/ABC283/tasks/abc283_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001


N = int(input())
A = list(map(int, input().split()))

ans = [-1] * N
for i in range(N):
    now = INF
    dif = 1
    while now>dif:
        if i-dif>=0:
            now = min(now, abs(A[i] - A[i-dif]) + abs(dif))
        if i+dif<N:
            now = min(now, abs(A[i] - A[i+dif]) + abs(dif))
        dif += 1
    ans[i] = now

print(*ans)
