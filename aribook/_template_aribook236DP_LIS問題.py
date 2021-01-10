# aribook236 DP 最長増加部分列問題(LIS: Longest Increasing Subsequence)

import numpy as np

MAX_N = 1000

N = int(input())
a = list(map(int, input().split()))

dp = np.zeros((N), np.int)   # DPテーブル

ans = 0
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    ans = max(ans, dp[i])

print(ans)

"""
input
N
a1 a2 .... an

testdata
5
4 2 3 1 5

output
3
"""
