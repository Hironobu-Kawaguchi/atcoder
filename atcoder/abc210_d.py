# https://atcoder.jp/contests/ABC210/tasks/abc210_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# import copy
INF = 1001001001001001
H, W, C = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
# dp = copy.deepcopy(A)
dp = [[0]*W for _ in range(H)]

ans = INF
for i in range(H):
    for j in range(W):
        dp[i][j] = A[i][j]
        if i!=0:
            ans = min(ans, dp[i-1][j]+C+A[i][j])
            dp[i][j] = min(dp[i][j], dp[i-1][j]+C)
        if j!=0:
            ans = min(ans, dp[i][j-1]+C+A[i][j])
            dp[i][j] = min(dp[i][j], dp[i][j-1]+C)
for i in range(H):
    for j in range(W-1, -1, -1):
        dp[i][j] = A[i][j]
        if i!=0:
            ans = min(ans, dp[i-1][j]+C+A[i][j])
            dp[i][j] = min(dp[i][j], dp[i-1][j]+C)
        if j!=W-1:
            ans = min(ans, dp[i][j+1]+C+A[i][j])
            dp[i][j] = min(dp[i][j], dp[i][j+1]+C)
# for i in range(H):
#     print(*A[i])
# for i in range(H):
#     print(*dp[i])

print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
