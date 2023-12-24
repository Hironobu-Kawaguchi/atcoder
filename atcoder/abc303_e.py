# https://atcoder.jp/contests/abc303/tasks/abc303_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

for u in range(N):
    if len(G[u]) == 1:
        start  = G[u][0]
        break

dist = [-1] * N
dist[start] = 0

q = deque([start])
while q:
    u = q.popleft()
    for v in G[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
stars = []
for u in range(N):
    if dist[u] % 3 == 0:
        stars.append(u)

ans = []
for u in stars:
    ans.append(len(G[u]))
ans.sort()
print(*ans)


# TLE
# N = int(input())
# G = [set() for _ in range(N)]
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     u -= 1; v -= 1
#     G[u].add(v)
#     G[v].add(u)
# deg = [len(G[u]) for u in range(N)]

# stars = []
# while True:
#     flg = False
#     for u in range(N):
#         if len(G[u]) == 1:  # 次数1の隣は星の中心
#             v = list(G[u])[0]
#             stars.append(v)
#             for w in G[v]:
#                 for x in G[w]:
#                     if x == v: continue
#                     G[x].remove(w)  # 星の辺を消す
#                 G[w] = set()   # 星の辺を消す
#             G[v] = set()       # 星の中心からの辺を消す
#             flg = True
#             # print(*G, file=sys.stderr)
#     if not flg:
#         break
# print(*stars, file=sys.stderr)

# ans = []
# for u in stars:
#     ans.append(deg[u])
# ans.sort()
# print(*ans)
