# aribook237 DP 分割数

import numpy as np

MAX_N = 1000
MAX_M = 1000
MOD = 10000

N, M = map(int, input().split())

dp = np.zeros((M+1, N+1), np.int)   # DPテーブル

dp[0, 0] = 1
for i in range(1, M+1):
    for j in range(N+1):
        if j -i  >= 0:
            dp[i, j] = (dp[i-1, j] + dp[i, j-i]) % MOD
        else:
            dp[i, j] = dp[i-1, j]

print(dp[M, N])

"""
input
N M

testdata
4 3

output
4
"""
