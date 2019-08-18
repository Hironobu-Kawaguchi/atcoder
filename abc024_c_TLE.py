# https://atcoder.jp/contests/abc024/tasks/abc024_c
# 解説通りの解法だが、PythonのためかTLE

import numpy as np
N, D, K = map(int, input().split())
DP = np.zeros((K, 2), np.int)

L, R = [], []
for i in range(D):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

S, T = [], []
for k in range(K):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)
    DP[k, :] = s

ans = [0] * K
for i in range(D):
    for k in range(K):
        if ans[k] == 0:
            if not (DP[k, 1] < L[i] or  DP[k, 0] > R[i]): # L-R の範囲外ではない
                DP[k, 0] = min(DP[k, 0], L[i])
                DP[k, 1] = max(DP[k, 1], R[i])
            if DP[k, 0] <= T[k] and DP[k, 1] >= T[k]:
                ans[k] = i+1
    if all(ans):
        break

for k in range(K):
    print(ans[k])
