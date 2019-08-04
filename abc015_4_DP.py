# https://atcoder.jp/contests/abc015/tasks/abc015_4

import numpy as np

Wmax = int(input())
n, k = map(int,input().split())

dp = np.zeros((k+1, Wmax+1), np.int)

for i in range(n):
  w, v = map(int,input().split())
  if w <= Wmax:
    dp[1:, w:] = np.maximum(dp[1:,w:], dp[:k,:Wmax+1-w]+v)
print(dp[k, Wmax])



# # import numpy as np
# MAX_N = 50
# MAX_U = 10000
# done = [[0] * (MAX_U + 1) for _ in range(MAX_N)]
# memo = [[0] * (MAX_U + 1) for _ in range(MAX_N)]

# W = int(input())
# N, K = map(int, input().split())
# A, B = [], []
# for i in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# # i番目以降の画像で、幅の総和がu以下、画像の枚数がj以下となるように選ぶ
# def search(i, j, u):
#     if i == N:
#         return 0
#     if done[i][u]:
#         return memo[i][u]
#     if u < A[i] or j == K:
#         res = search(i+1, j, u)
#     else:
#         res = max(search(i+1, j, u), search(i+1, j+1, u-A[i]) + B[i])
#     done[i][u] = 1
#     memo[i][u] = res
#     return res

# ans = search(0, 0, W)

# print(ans)
