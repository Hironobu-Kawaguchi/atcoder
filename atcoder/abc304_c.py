# https://atcoder.jp/contests/abc304/tasks/abc304_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N, D = map(int, input().split())
xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))

A = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2 <= D ** 2:
            A[i][j] = True
# print(A)

ans = [False] * N
ans[0] = True

def dfs(u):
    for v in range(N):
        if A[u][v] and not ans[v]:
            ans[v] = True
            dfs(v)
dfs(0)

for i in range(N):
    if ans[i]:
        print("Yes")
    else:
        print("No")
