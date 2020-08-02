# https://atcoder.jp/contests/abc063/tasks/arc075_a

import numpy as np
N = int(input())
MAX_V = 10001
s = [int(input()) for _ in range(N)]

dp = np.zeros((N+1, MAX_V), np.int)
dp[0, 0] = 1
for i in range(N):
    for j in range(MAX_V):
        if dp[i, j]:
            dp[i+1, j] = 1
            dp[i+1, j + s[i]] = 1

for ans in range(MAX_V-1, -1, -1):
    if dp[N, ans]:
        if ans % 10 or ans == 0:
            print(ans)
            break
