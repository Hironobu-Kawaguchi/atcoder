# https://atcoder.jp/contests/abc309/tasks/abc309_e
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque

N, M = map(int, input().split())
p = list(map(int, (input().split())))
G = [[] for _ in range(N)]
for i in range(N-1):
    G[p[i]-1].append(i+1)
hoken = [-1] * N
for i in range(M):
    x, y = map(int, input().split())
    hoken[x-1] = max(hoken[x-1], y)

def bfs():
    q = deque([(0, hoken[0])])
    while q:
        now, y = q.popleft()
        for nxt in G[now]:
            ny = max(y-1, hoken[nxt])
            hoken[nxt] = ny
            q.append((nxt, ny))
    return

bfs()
ans = 0
for i in range(N):
    if hoken[i]>=0:
        ans += 1
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
