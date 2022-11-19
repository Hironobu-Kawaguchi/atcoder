# https://atcoder.jp/contests/abc211/tasks/abc211_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import deque
MOD = 10**9+7

N, M = map(int, input().split())
to = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)

dist = [-1]*N
cnt = [0]*N
q = deque()
q.append((0, 1, -1))
while len(q):
    now, d, pre = q.popleft()
    if dist[now]==-1:
        dist[now] = d
        for nxt in to[now]:
            if dist[nxt]!=-1 and dist[nxt]!=d+1: continue
            q.append((nxt, d+1, now))
    elif dist[now]!=d: continue
    cnt[now] += cnt[pre] if pre!=-1 else 1
    cnt[now] %= MOD

# print(dist)
# print(cnt)
print(cnt[N-1])


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
