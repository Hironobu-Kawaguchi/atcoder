# https://atcoder.jp/contests/arc107/tasks/arc107_b
import numpy as np

N, K = map(int, input().split())
dp = np.zeros(3*N, dtype=np.int64)
dp[2:N+2] = dp[2:N+2] + np.arange(1,N+1)
dp[N+2:2*N+1] = dp[N+2:2*N+1] + np.arange(1,N)[::-1]
cum = np.cumsum(dp)
# print(dp)

dp = np.zeros(3*N, dtype=np.int64)
for i in range(2*N):
    dp[i] = cum[i+N] - cum[i]
cum = np.cumsum(dp)
# print(dp)

dp = np.zeros(3*N, dtype=np.int64)
for i in range(2*N):
    dp[i] = cum[i+N] - cum[i]
print(dp[abs(K)])
# print(cum)

