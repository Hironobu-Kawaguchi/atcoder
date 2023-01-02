# https://atcoder.jp/contests/typical90/tasks/typical90_ap

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
K = int(input())
# 数字が9の倍数になるのは，各桁の合計Kが９の倍数のとき
# 各桁の合計Kを切断する場所はK-1箇所あり，切断有無の組み合わせは2^(K-1)通り
# ただし連続で使えるのは9個まで
# 合計Kの組み合わせは，合計K-1,....,K-9の組み合わせの和になるのでDP
if K%9==0:
    dp = [0] * (K+1)
    dp[0] = 1
    for i in range(1,K+1):
        for j in range(i-1, max(-1, i-10), -1):
            dp[i] += dp[j]
        dp[i] %= MOD
    # print(dp)
    ans = dp[K]

    # dp = [[0]*9 for _ in range(K)]
    # dp[0][0] = 1
    # for i in range(K-1):
    #     for j in range(9):
    #         dp[i+1][0] += dp[i][j]
    #         if j!=8: dp[i+1][j+1] += dp[i][j]
    #     for j in range(9):
    #         dp[i+1][j] %= MOD
    # ans = 0
    # for j in range(9):
    #     ans += dp[K-1][j]
    #     ans %= MOD

    # ans = pow(2, K-1, MOD)

    print(ans)
else:
    print(0)
