# aribook235 DP 個数制限付き部分和問題

import numpy as np

MAX_N = 100
MAX_K = 100

N, K = map(int, input().split())
a, m = [], []
for i in range(N):
    a_, m_ = map(int, input().split())
    a.append(a_)
    m.append(m_)

dp = np.full((K+1), -1, np.int)   # 全要素-1のndarray
dp[0] = 0

for i in range(N):
    for j in range(K+1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif (j < a[i] or dp[j - a[i]] <= 0):
            dp[j] = -1
        else:
            dp[j] = dp[j - a[i]] - 1

if dp[K] >= 0:
    print("Yes")
else:
    print("No")

"""
input
N K
a1 m1
an mn

testdata
3 17
3 3
5 2
8 2

output
Yes
"""
