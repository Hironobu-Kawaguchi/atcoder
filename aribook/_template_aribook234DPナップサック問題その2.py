# aribook234 DP ナップサック問題その2

import numpy as np

MAX_N = 100
MAX_W = 1000000000
MAX_V = 100

N, W = map(int, input().split())
w, v = [], []
for i in range(N):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)

dp = np.zeros((N+1, MAX_N * MAX_V + 1), np.int)
dp[0, 1:] = MAX_W + 1

for i in range(N):
    for j in range(MAX_N * MAX_V + 1):
        if j < v[i]:
            dp[i+1, j] = dp[i, j]
        else:
            dp[i+1, j] = min(dp[i, j], dp[i, j-v[i]] + w[i])

ans = 0
for i in range(MAX_N * MAX_V + 1):
    if dp[N, i] <= W:
        ans = i
print(ans)


"""
input
N W
w1 v1
wn vn

testdata
4 5
2 3
1 2
3 4
2 2

output
7
"""
