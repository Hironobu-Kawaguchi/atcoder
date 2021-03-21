# https://atcoder.jp/contests/abc044/tasks/arc060_a

import numpy as np
N, A = map(int, input().split())
x = list(map(int, input().split()))

dp = np.zeros((51, 5001), np.int64)  # 50 * 50 = 2500
dp[0, 2500] = 1   # 2500:0, 0:-2500, 5000:2500

for i in range(N):
    for j in range(5001):
        if dp[i, j] != 0:
            dp[i+1, j] += dp[i, j]
            dp[i+1, j+x[i]-A] += dp[i, j]
print(dp[N, 2500] - 1)  # 1つも選ばないパターンを引く
