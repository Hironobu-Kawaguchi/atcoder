# https://atcoder.jp/contests/typical90/tasks/typical90_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
to = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append(B)
    to[B].append(A)
# print(to)

dist = [-1] * N

def dfs(n, u):
    dist[u] = n
    for v in to[u]:
        if dist[v]==-1:
            dfs(n+1, v)
    return

def check_dist(start):
    global dist
    dist = [-1] * N
    dfs(0, start)
    max_idx = -1
    max_d = 0
    for i in range(N):
        if dist[i]>max_d:
            max_d = dist[i]
            max_idx = i
    return max_idx, max_d

max_idx, _ = check_dist(0)
# print(dist, max_idx)
max_idx, max_d = check_dist(max_idx)
# print(dist)
print(max_d + 1)


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
