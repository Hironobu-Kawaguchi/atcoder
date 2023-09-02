# https://atcoder.jp/contests/abc305/tasks/abc305_e
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import heapq

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
keibi = [-1] * N
q = []
for i in range(K):
    p, h = map(int, input().split())
    p -= 1
    keibi[p] = h
    heapq.heappush(q, (-h, p))

while q:
    h, p = heapq.heappop(q)
    h = -h
    if keibi[p] > h: continue
    # keibi[p] = h
    if h == 0: continue
    for np in G[p]:
        if keibi[np] < h-1:
            keibi[np] = h-1
            heapq.heappush(q, (-h+1, np))

ans = []
for i in range(N):
    if keibi[i] >= 0:
        ans.append(i+1)
print(len(ans))
print(*ans)
