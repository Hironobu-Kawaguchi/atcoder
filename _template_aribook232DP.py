# aribook232 DP 最長共通部分列問題

import numpy as np

MAX_N = 1000
MAX_M = 1000

N, M = map(int, input().split())
s = input()
t = input()

dp = np.zeros((N+1, M+1), np.int)

for i in range(N):
    for j in range(M):
        if s[i] == t[j]:
            dp[i+1, j+1] = dp[i, j] + 1
        else:
            dp[i+1, j+1] = max(dp[i, j+1], dp[i+1, j])

print(dp[N, M])


"""
input
N M
s
t

testdata
4 4
abcd
becd

output
3
"""
