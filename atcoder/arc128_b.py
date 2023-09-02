# https://atcoder.jp/contests/arc128/tasks/arc128_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
INF = 10 ** 10

def main():
    RGB = list(map(int, input().split()))
    ans = INF
    for i in range(3):
        rest = [RGB[j] for j in range(3) if j!=i]
        rest.sort()
        if (rest[1]-rest[0])%3==0:
            ans = min(ans, rest[1])
    if ans==INF:
        print(-1)
    else:
        print(ans)

T = int(input())
for _ in range(T):
    main()

# TLE
# N = int(input())
# A = list(map(int, (input().split())))
# dp = [[[0] * 2 for _ in range(2)] for _ in range(N+1)]
# dp[0][0][0], dp[0][0][1] = 1, 1
# for i in range(N):
#     # A[i]を使わない
#     for j in range(2):
#         for k in range(2):
#             dp[i+1][j][k] += dp[i][j][k]
#     # A[i]を使う
#     if i==0 or dp[i][0][0]*A[i]*dp[i+1][1][1] > dp[i][0][1]*dp[i+1][1][0]:
#         dp[i+1][1][0] = dp[i][0][0] * A[i]
#         dp[i+1][1][1] = dp[i][0][1]
#     if dp[i][1][0]*dp[i+1][0][1] > dp[i][1][1]*A[i]*dp[i+1][0][0]:
#         dp[i+1][0][0] = dp[i][1][0]
#         dp[i+1][0][1] = dp[i][1][1] * A[i]
# # print(dp[N][0][0]/dp[N][0][1])
# ans = []
# now = 0
# for i in range(N-1, -1, -1):
#     if now==0:
#         if i==0:
#             ans.append(0)
#             continue
#         if dp[i][1][0]*dp[i+1][0][1] == dp[i][1][1]*A[i]*dp[i+1][0][0]:
#             ans.append(1)
#             now = 1 - now
#         else:
#             ans.append(0)
#     else:
#         if dp[i][0][0]*A[i]*dp[i+1][1][1] == dp[i][0][1]*dp[i+1][1][0]:
#             ans.append(1)
#             now = 1 - now
#         else:
#             ans.append(0)
# print(*ans[::-1])

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
