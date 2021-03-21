# https://atcoder.jp/contests/abc187/tasks/abc187_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# sys.setrecursionlimit(10 ** 7)
# from itertools import product

import sys
input = sys.stdin.buffer.readline

diff = []
suma = 0
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    diff.append(2*a+b)
    suma -= a
diff.sort(reverse=True)
for i in range(n):
    suma += diff[i]
    if suma > 0:
        ans = i+1
        break
print(ans)

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


# TLE
# import sys
# input = sys.stdin.buffer.readline
# import copy
# INF = 1001001001001001

# n = int(input())
# dp = [-INF]*(n+1)
# dp[0] = 0
# for i in range(n):
#     dpnext = [-INF]*(n+1)
#     a, b = map(int, input().split())
#     for j in range(n+1):
#         if j:
#             dpnext[j] = max(dp[j]-a, dp[j-1]+a+b)
#         else:
#             dpnext[j] = dp[j]-a
#     dp = copy.copy(dpnext)
# ans = n
# for i in range(n+1):
#     if dp[i] > 0:
#         ans = i
#         break
# print(ans)
