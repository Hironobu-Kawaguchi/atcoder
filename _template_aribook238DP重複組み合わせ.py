# aribook238 DP 重複組み合わせ

import numpy as np

MAX_N = 1000
MAX_M = 1000
MOD = 10000

N, M = map(int, input().split())
a = list(map(int, input().split()))

dp = np.zeros((N+1, M+1), np.int)   # DPテーブル

dp[:, 0] = 1    # 1つも選ばない方法は常に一通り
for i in range(N):
    for j in range(1, M+1):
        if j - 1 - a[i] >= 0:
            # 引き算が含まれる場合には負の数にならないように注意する
            dp[i+1, j] = (dp[i+1, j-1] + dp[i, j] - dp[i, j-1-a[i]] + MOD) % MOD
        else:
            dp[i+1, j] = (dp[i+1, j-1] + dp[i, j]) % MOD

print(dp[M, N])

"""
input
N M
a1 a2 ... an

testdata
3 3
1 2 3

output
6
"""
