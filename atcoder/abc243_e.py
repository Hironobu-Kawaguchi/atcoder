# https://atcoder.jp/contests/abc243/tasks/abc243_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001001

N, M = map(int, input().split())
to = []
for i in range(M):
    A, B, C = map(int, input().split())
    to.append((A-1, B-1, C))

dist = [[INF]*N for _ in range(N)]
# for i in range(N): dist[i][i] = 0

for a, b, c in to:
    dist[a][b] = c
    dist[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
ans = 0
for a, b, c in to:
    unused = 0
    for i in range(N):
        if dist[a][i] + dist[i][b] <= c:
            unused = 1
            break
    ans += unused
# print(dist)
print(ans)


# TLE
# import heapq
# import networkx as nx
# INF = 1001001001001

# N, M = map(int, input().split())
# to = [[] for _ in range(N)]
# for i in range(M):
#     A, B, C = map(int, input().split())
#     to[A-1].append((B-1, C))
#     to[B-1].append((A-1, C))

# dist = [[INF]*N for _ in range(N)]
# q = []
# G = nx.Graph()
# G.add_node(0)
# for b, c in to[0]:
#     heapq.heappush(q, (c, 0, b))

# while q:
#     c, a, b = heapq.heappop(q)
#     if b in G.nodes():
#         if c < nx.dijkstra_path_length(G, source=a, target=b):
#         # print(c, a, b, dist[a][b])
#         # if c < dist[a][b]:
#             G.add_edge(a, b, weight=c)
#             for b2, c in to[b]:
#                 heapq.heappush(q, (c, b, b2))
#     else:
#         G.add_edge(a, b, weight=c)
#         length = nx.single_source_dijkstra_path_length(G, b)
#         for n, l in length.items():
#             dist[b][n] = l
#             dist[n][b] = l
#         for b2, c in to[b]:
#             heapq.heappush(q, (c, b, b2))

# # print(G.nodes(), G.edges(), len(G.edges()))
# print(M - len(G.edges()))


