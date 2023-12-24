# https://atcoder.jp/contests/abc309/tasks/abc309_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
from collections import deque

N1, N2, M = map(int, input().split())
N = [N1, N2]
G1, G2 = [[] for _ in range(N1)], [[] for _ in range(N2)]
G = [G1, G2]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if a<N1:
        G1[a].append(b)
        G1[b].append(a)
    else:
        G2[a-N1].append(b-N1)
        G2[b-N1].append(a-N1)

def bfs(G, s):
    dist = [-1] * len(G)
    dist[s] = 0
    q = deque([s])
    while q:
        now = q.popleft()
        for nxt in G[now]:
            if dist[nxt]==-1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    return dist[now]

def dfs(G, now, d, dist):
    dist[now] = d
    for nxt in G[now]:
        if dist[nxt]==-1 or dist[nxt]>d+1:
            dfs(G, nxt, d+1, dist)
    return

def max_dist(idx, s):
    # dist = [-1] * N[idx]
    # dfs(G[idx], s, 0, dist)
    # return max(dist)
    return bfs(G[idx], s)

# print(max_dist(0, 0), max_dist(1, N2-1), file=sys.stderr)
ans = max_dist(0, 0) + max_dist(1, N2-1) + 1
print(ans)


# for a in range(1,9):
#     for b in range(a+1, 10):
#         main(a, b)

# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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


# for a in range(1,9):
#     for b in range(a+1, 10):
#         main(a, b)

# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
