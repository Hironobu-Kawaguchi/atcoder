# https://atcoder.jp/contests/abc251/tasks/abc251_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
INF = 100100100100

N = int(input())
A = list(map(int, (input().split())))

dp = [[0]*4 for _ in range(N)]
# 0: 直近選択+1選択、1: 直近選択+1未選択、2: 直近未選択+1選択、3: 直近未選択+1未選択
dp[0][0] = A[0]
dp[0][1] = INF
dp[0][2] = A[0]

for i in range(1, N-1):
    dp[i][0] = min(dp[i-1][0] + A[i], dp[i-1][2] + A[i])
    dp[i][1] = min(dp[i-1][1] + A[i], dp[i-1][3] + A[i])
    dp[i][2] = dp[i-1][0]
    dp[i][3] = dp[i-1][1]

ans = min(dp[N-2][0], dp[N-2][1]+A[N-1], dp[N-2][2]+A[N-1], dp[N-2][3]+A[N-1])
print(ans)
# for i in range(N):
#     print(dp[i])


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
