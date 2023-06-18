# https://atcoder.jp/contests/arc159/tasks/arc159_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
from collections import deque

def main():
    N, K = map(int, input().split())
    A = [list(map(int, (input().split()))) for _ in range(N)]
    to = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                to[i].append(j)
    Q = int(input())

    def bfs(s, t):
        flg = s==t
        s -= 1
        s %= N
        t -= 1
        t %= N
        q = deque()
        q.append(s)
        dist = [-1]*N
        dist[s] = 0
        while q:
            v = q.popleft()
            for u in to[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + 1
                    if u==t:
                        print(dist[t])
                        return
                    q.append(u)
                elif u==t:
                    print(dist[v] + 1)
                    # print(qi, dist)
                    return
        print(-1)
        # print(qi, dist)
        return

    for qi in range(Q):
        s, t = map(int, input().split())
        bfs(s, t)
    return

main()

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
