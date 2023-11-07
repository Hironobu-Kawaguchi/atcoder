# https://atcoder.jp/contests/abc320/tasks/abc320_d
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque

INF = 10**18

N, M = map(int, input().split())
# uf = UnionFind(N)
G = [[] for _ in range(N)]
for i in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1; B -= 1
    G[A].append((B, X, Y))
    G[B].append((A, -X, -Y))
# print(G)

gone = [False] * N
ng = [False] * N
xy = [[INF, INF]for _ in range(N)]
xy[0] = [0, 0]

# def dfs(now):
#     global flg
#     if gone[now]:
#         return
#     gone[now] = True
#     for to, x, y in G[now]:
#         if gone[to]:
#             if xy[to] != [xy[now][0] + x, xy[now][1] + y]:
#                 ng[to] = True
#                 # flg = False
#                 # return
#         else:
#             xy[to] = [xy[now][0] + x, xy[now][1] + y]
#             dfs(to)
#     return

# dfs(0)
# print(xy)

# bfs
q = deque([(0, 0, 0)])
while q:
    now, x, y = q.popleft()
    if gone[now]:
        if xy[now] != [x, y]:
            ng[now] = True
        continue
    gone[now] = True
    for to, dx, dy in G[now]:
        nx = x + dx
        ny = y + dy
        xy[to] = [nx, ny]
        q.append((to, nx, ny))

print(0, 0)
for i in range(1, N):
    if xy[i] == [INF, INF] or ng[i]:
        print("undecidable")
    else:
        print(xy[i][0], xy[i][1])
