# https://atcoder.jp/contests/abc306/tasks/abc306_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))
dp = [[0]*2 for _ in range(N+1)]
for i in range(N):
    if xy[i][0] == 1:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][0] + xy[i][1], dp[i][1])
    else:
        dp[i+1][0] = max(dp[i][0], max(dp[i][0], dp[i][1]) + xy[i][1])
        dp[i+1][1] = dp[i][1]
# print(dp)
print(max(dp[N][0], dp[N][1]))

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
