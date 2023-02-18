# https://atcoder.jp/contests/abc288/tasks/abc288_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
INF = 1001001001001001

N, M = map(int, input().split())
A = list(map(int, (input().split())))
C = list(map(int, (input().split())))
X = list(map(int, (input().split())))

dp = [[INF]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
# for i in range(N+1):
#     dp[i][0] = 0
cost = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(i+1):
        if j==0:
            cost[i][j] = C[i]
        else:
            cost[i][j] = min(cost[i][j-1], C[i-j])
# for i in range(N):
#     print(cost[i])

idx = 0
for i in range(N):
    for j in range(i+1):
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + A[i] + cost[i][j])
        if idx<M and i==X[idx]-1: continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    if idx<M and i==X[idx]-1:
        idx += 1
# for i in range(N+1):
#     print(dp[i])

ans = INF
for j in range(M, N+1):
    ans = min(ans, dp[N][j])
# for i in range(M):
#     ans += A[X[i]-1]
print(ans)



# WA
# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# import copy

# N, M = map(int, input().split())
# A = list(map(int, (input().split())))
# C = list(map(int, (input().split())))
# X = list(map(int, (input().split())))
# ans = 0
# for i in range(M):
#     ans += A[X[i]-1]
# pre = [[]]
# idx = 0
# for i in range(N):
#     jj = 0
#     if i==X[idx]-1:
#         v = C[X[idx]-1]
#         u = X[idx] - 1
#         for j in range(idx):
#             if C[X[idx]-1-j]<v:
#                 v = C[X[idx]-1-j]
#                 u = X[idx] - 1
#         for j in range(len(pre[u])):
#             # print(u, j, pre[u])
#             if j<jj:
#                 if C[u-j-1]: break
#                 v = C[u-j-1]
#             else:
#                 if v<pre[u][j]+C[u-j-1]: break
#                 v = pre[u][j]+C[u-j-1]
#                 jj = max(jj, j+1)
#         ans += v
#         print(ans, idx, v, u)
#         idx += 1
#     pre.append(copy.copy(pre[-1]))
#     pre[-1].append(A[i] + C[i])
#     pre[-1].sort()
# # print(pre)
# print(ans)

