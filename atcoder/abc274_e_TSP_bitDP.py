# https://atcoder.jp/contests/abc274/tasks/abc274_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1e18

N, M = map(int, input().split())
W = N+M+1
pos = []
for i in range(N+M):
    pos.append(tuple(map(int, input().split())))
pos.append((0,0)) # 原点
# print(pos)

Wbit = 1<<W
dp = [[INF]*W for _ in range(Wbit)]
dp[0][N+M] = 0
sp = [1.0]*Wbit
for s in range(Wbit):
    for v in range(N, N+M):
        if ((s>>v)&1): sp[s] /= 2
# print(sp)

dist = [[INF]*W for _ in range(W)]
for v in range(W):
    for u in range(W):
        dist[v][u] = ((pos[v][0]-pos[u][0])**2 + (pos[v][1]-pos[u][1])**2)**0.5
# print(dist)

for s in range(Wbit):
    for v in range(W):
        if dp[s][v]==INF: continue
        for u in range(W):
            if ((s>>u)&1): continue
            dp[s|(1<<u)][u] = min(dp[s|(1<<u)][u], dp[s][v] + dist[v][u]*sp[s])
# print(dp)

t = (1<<N)-1 | (1<<(N+M))

ans = INF
for s in range(Wbit):
    if ((s&t)==t):
        ans = min(ans, dp[s][N+M])
print(ans)



# TLE
# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# N, M = map(int, input().split())
# XY = [[int(xy) for xy in input().split()] for _ in range(N)]
# # print(XY)
# PQ = [[int(pq) for pq in input().split()] for _ in range(M)]
# # print(PQ)

# ans = 1001001001001.0

# def dfs(dist, x, y, cnt, speed, gone):
#     global ans
#     if cnt==N:
#         dist += ((x*x + y*y)**0.5)/speed
#         # print(ans, dist, cnt, speed, gone)
#         if dist<ans: ans = dist
#         return
#     for i in range(N+M):
#         if gone[i]: continue
#         gone[i] = True
#         if i<N:
#             nx, ny = XY[i]
#             move = (((nx-x)**2 + (ny-y)**2)**0.5)/speed
#             dfs(dist + move, nx, ny, cnt + 1, speed, gone)
#         else:
#             nx, ny = PQ[i-N]
#             move = (((nx-x)**2 + (ny-y)**2)**0.5)/speed
#             dfs(dist + move, nx, ny, cnt, speed * 2, gone)
#         gone[i] = False
#     return

# dfs(0, 0, 0, 0, 1, [False]*(N+M))
# print(ans)

