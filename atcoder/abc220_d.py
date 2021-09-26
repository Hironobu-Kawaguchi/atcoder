# https://atcoder.jp/contests/abc220/tasks/abc220_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N = int(input())
A = list(map(int, (input().split())))
dp = [[0]*10 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(N-1):
    for j in range(10):
        if dp[i][j]==0: continue
        dp[i+1][(j+A[i+1])%10] += dp[i][j]
        dp[i+1][(j+A[i+1])%10] %= MOD
        dp[i+1][(j*A[i+1])%10] += dp[i][j]
        dp[i+1][(j*A[i+1])%10] %= MOD
for j in range(10):
    print(dp[N-1][j])


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
