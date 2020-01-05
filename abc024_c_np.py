# https://atcoder.jp/contests/abc024/tasks/abc024_c

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
import numpy as np

N,D,K = map(int,readline().split())
LRST = np.array(read().split(),np.int64).reshape(-1,2)
LR = LRST[:D].tolist()
ST = LRST[D:]

x = np.zeros((D+1,K),np.int64) # 移動可能な左端
y = np.zeros((D+1,K),np.int64) # 移動可能な右端
x[0] = ST[:,0]
y[0] = ST[:,0]

for day,(L,R) in enumerate(LR,1):
    bl = (L<=x[day-1])&(x[day-1]<=R)
    x[day] = x[day-1]; x[day][bl] = L
    bl = (L<=y[day-1])&(y[day-1]<=R)
    y[day] = y[day-1]; y[day][bl] = R

answer = ((x > ST[:,1]) | (y < ST[:,1])).sum(axis=0)
print('\n'.join(answer.astype(str)))


# # 解説通りの解法だが、PythonのためかTLE
# import numpy as np
# N, D, K = map(int, input().split())
# DP = np.zeros((K, 2), np.int)

# L, R = [], []
# for i in range(D):
#     l, r = map(int, input().split())
#     L.append(l)
#     R.append(r)

# S, T = [], []
# for k in range(K):
#     s, t = map(int, input().split())
#     S.append(s)
#     T.append(t)
#     DP[k, :] = s

# ans = [0] * K
# for i in range(D):
#     for k in range(K):
#         if ans[k] == 0:
#             if not (DP[k, 1] < L[i] or  DP[k, 0] > R[i]): # L-R の範囲外ではない
#                 DP[k, 0] = min(DP[k, 0], L[i])
#                 DP[k, 1] = max(DP[k, 1], R[i])
#             if DP[k, 0] <= T[k] and DP[k, 1] >= T[k]:
#                 ans[k] = i+1
#     if all(ans):
#         break

# for k in range(K):
#     print(ans[k])
