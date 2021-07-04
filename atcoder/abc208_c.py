# https://atcoder.jp/contests/abc208/tasks/abc208_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
a = list(map(int, (input().split())))
ai = []
for i in range(N):
    ai.append([a[i],i])
ai.sort()
# print(ai)
for i in range(N):
    a[ai[i][1]] = i
# print(a)

q, mod = divmod(K, N)
for i in range(N):
    if a[i]<mod:
        print(q+1)
    else:
        print(q)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
