# https://atcoder.jp/contests/typical90/tasks/typical90_bz
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
to = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    if a>b:
        to[a-1].append(b-1)
    else:
        to[b-1].append(a-1)
ans = 0
for i in range(N):
    if len(to[i])==1:
        ans += 1
print(ans)


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
