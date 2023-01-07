# https://atcoder.jp/contests/typical90/tasks/typical90_m
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import heapq
INF = 1001001001

N, M = map(int, input().split())
to = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    to[a-1].append([b-1, c])
    to[b-1].append([a-1, c])
# print(to)

def dijkstra(start: int):
    cost_list = [INF]*N
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cc, u = heapq.heappop(q)
        # print(u, cc)
        if cost_list[u]!=INF: continue
        cost_list[u] = cc
        for v, c in to[u]:
            heapq.heappush(q, (cc+c, v))
    return cost_list

cost1 = dijkstra(0)
costN = dijkstra(N-1)
for i in range(N):
    print(cost1[i] + costN[i])
