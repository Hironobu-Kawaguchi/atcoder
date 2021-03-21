# aribook231 DP ナップサック問題

import numpy as np

MAX_N = 100
MAX_W = 10000

N, W = map(int, input().split())
w, v = [], []
for i in range(N):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)

# i番目以降の品物から重さの総和がj以下となるように選ぶ
dp = np.zeros((N+1, W+1), np.int)

for i in range(N-1, -1, -1):
    for j in range(W+1):
        if j < w[i]:
            dp[i, j] = dp[i+1, j]
        else:
            dp[i, j] = max(dp[i+1, j], dp[i+1, j-w[i]] + v[i])

print(dp[0, W])


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
