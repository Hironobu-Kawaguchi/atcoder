# https://atcoder.jp/contests/abc320/tasks/abc320_e
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import heapq

N, M = map(int, input().split())

# sentou_idx = 0
q = []
ans = [0] * N
ready_q = []
for i in range(N):
    heapq.heappush(ready_q, i)
for _ in range(M):
    t, w, s = map(int, input().split())
    while q and q[0][0] <= t:
        _, j, _ = heapq.heappop(q)
        heapq.heappush(ready_q, j)
    if len(ready_q)==0:
        continue
    ans[ready_q[0]] += w
    heapq.heappush(q, (t + s, ready_q[0], w))
    _ = heapq.heappop(ready_q)
for i in range(N):
    print(ans[i])
