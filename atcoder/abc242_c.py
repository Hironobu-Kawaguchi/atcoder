# https://atcoder.jp/contests/abc242/tasks/abc242_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N = int(input())
dp = [[0]*11 for _ in range(N)]

for j in range(1, 10):
    dp[0][j] = 1
# print(*dp[0])

for i in range(N-1):
    for j in range(1, 10):
        dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
        dp[i+1][j] %= MOD
    # print(*dp[i+1])

ans = 0
for j in range(1, 10):
    ans += dp[N-1][j]
    ans %= MOD

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
