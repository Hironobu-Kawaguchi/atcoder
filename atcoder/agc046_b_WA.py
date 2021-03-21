# https://atcoder.jp/contests/agc046/tasks/agc046_b
# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# # フェルマーの小定理
# def nCr(n, r, mod=MOD):
#     r = min(r, n-r)
#     numer = denom = 1
#     for i in range(1, r+1):
#         numer = numer * (n+1-i) % mod
#         denom = denom * i % mod
#     return numer * pow(denom, mod-2, mod) % mod

MOD = 998244353
A, B, C, D = map(int, input().split())
H = C-A+1
W = D-B+1
dp = [[0]*(W+1) for _ in range(H+1)]
dp[1][1] = 1
mods = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        if i==0 and j==0: continue
        # if i==0 or j==0:
        #     dp[i+1][j+1] = dp[i+1][j] * (A+i) + dp[i][j+1] * (B+j)
        # else:
        #     dp[i+1][j+1] = max(dp[i+1][j] * (A+i) + dp[i][j+1] , dp[i+1][j] + dp[i][j+1] * (B+j))
        #     # dp[i+1][j+1] = dp[i+1][j] * (A+i) + dp[i][j+1] * (B+j) - nCr(max(dp[i+1][j],dp[i][j+1]), min(dp[i+1][j],dp[i][j+1]))
        #     # print(nCr(max(dp[i+1][j],dp[i][j+1]), min(dp[i+1][j],dp[i][j+1])))
        # if mods[i+1][j] > mods[i][j+1]:
        #     dp[i+1][j+1] = dp[i+1][j] * (A+i) + dp[i][j+1]
        #     mods[i+1][j+1] = mods[i+1][j]
        # elif mods[i+1][j] < mods[i][j+1]:
        #     dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] * (B+j)
        #     mods[i+1][j+1] = mods[i][j+1]
        # else:
        #     dp[i+1][j+1] = max(dp[i+1][j] * (A+i) + dp[i][j+1] , dp[i+1][j] + dp[i][j+1] * (B+j))
        #     mods[i+1][j+1] = max(mods[i+1][j], mods[i][j+1])
        # div, mod = divmod(dp[i+1][j+1], MOD)
        # dp[i+1][j+1] = mod
        # mods[i+1][j+1] += div
        dp[i+1][j+1] = max(dp[i+1][j] * (A+i) + dp[i][j+1] , dp[i+1][j] + dp[i][j+1] * (B+j))
        dp[i+1][j+1] %= MOD
# print(dp)
print(dp[H][W])
# print(dp[H][W] % MOD)


# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
