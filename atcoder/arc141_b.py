# https://atcoder.jp/contests/arc141/tasks/arc141_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

def main():
    N, M = map(int, input().split())
    now = 1
    for i in range(N-1):
        if now > M:
            print(0)
            return
        now *= 2
    # TLE
    # if pow(2, N-1)>M:
    #     print(0)
    #     return
    dp = [[0] * 62 for _ in range(N)]
    now = 1
    for i in range(62):
        if now > M: break
        dp[0][i] = min(M - now + 1, now)
        now *= 2
        # now %= MOD

    for i in range(1, N):
        cum = 0
        now = 1
        for j in range(62):
            if now > M: break
            dp[i][j] = (dp[0][j] * cum) % MOD
            cum += dp[i-1][j]
            cum %= MOD
            now *= 2
            now %= MOD
    # for i in range(N):
    #     print(dp[i])

    ans = 0
    for i in range(62):
        ans += dp[N-1][i]
        ans %= MOD
    print(ans)
    return

main()

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
