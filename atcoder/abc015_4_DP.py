# https://atcoder.jp/contests/abc015/tasks/abc015_4

import numpy as np

W = int(input())
N, K = map(int,input().split())

dp = np.zeros((K+1, W+1), np.int)

for i in range(N):
  A, B = map(int,input().split())
  if A <= W:
    dp[1:, A:] = np.maximum(dp[1:,A:], dp[:K,:W+1-A]+B)
print(dp[K, W])


# import numpy as np

# W = int(input())
# N, K = map(int,input().split())

# dp = np.zeros((K+1, W+1), np.int)

# for i in range(N):
#   A, B = map(int,input().split())
#   if A <= W:
#     dp[1:, A:] = np.maximum(dp[1:,A:], dp[:K,:W+1-A]+B)
# print(dp[K, W])
