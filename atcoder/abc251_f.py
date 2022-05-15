# https://atcoder.jp/contests/abc251/tasks/abc251_f
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
from collections import deque
INF = 100100100100

N, M = map(int, input().split())
to = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    to[u-1].append(v-1)
    to[v-1].append(u-1)

# DFS
T1 = []
done = [False] * N
done[0] = True

def dfs(u):
    for v in to[u]:
        if done[v]: continue
        done[v] = True
        T1.append([u+1, v+1])
        dfs(v)
    return

dfs(0)
for (x, y) in T1:
    print(x, y)

# BFS
T2 = []
done = [False] * N
q = deque()
q.append([0,-1])
while q:
    now, pre = q.popleft()
    if done[now]: continue
    done[now] = True
    if now!=0:
        T2.append([pre+1, now+1])
    for v in to[now]:
        if done[v]: continue
        q.append([v, now])
for (z, w) in T2:
    print(z, w)


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
