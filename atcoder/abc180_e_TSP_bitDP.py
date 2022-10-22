# https://atcoder.jp/contests/abc180/tasks/abc180_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1e18

N = int(input())
pos = []
for i in range(N):
    pos.append(tuple(map(int, input().split())))
# print(pos)
dist = [[INF]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = abs(pos[j][0]-pos[i][0]) + abs(pos[j][1]-pos[i][1]) + max(0, pos[j][2]-pos[i][2])
# print(dist)

Nbit = 1<<N
dp = [[INF]*N for _ in range(Nbit)]
dp[0][0] = 0
for s in range(Nbit):
    for i in range(N):
        if dp[s][i]==INF: continue
        for j in range(N):
            if (s>>j&1): continue
            dp[s|(1<<j)][j] = min(dp[s|(1<<j)][j], dp[s][i] + dist[i][j])
# print(dp)
print(dp[Nbit-1][0])

