# https://atcoder.jp/contests/ABC212/tasks/abc212_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353
N, M, K = map(int, input().split())
uv = []
for i in range(M):
    U, V = map(int, input().split())
    uv.append([U-1, V-1])
# print(uv)
dp = [[0]*N for _ in range(K+1)]
dp[0][0] = 1
for i in range(K):
    sm = sum(dp[i])
    for j in range(N):
        dp[i+1][j] = sm
    for j in range(M):
        dp[i+1][uv[j][0]] -= dp[i][uv[j][1]]
        dp[i+1][uv[j][1]] -= dp[i][uv[j][0]]
    for j in range(N):
        dp[i+1][j] -= dp[i][j]
        dp[i+1][j] = dp[i+1][j] % MOD
# print(dp)
print(dp[K][0])


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
