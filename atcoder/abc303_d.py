# https://atcoder.jp/contests/abc303/tasks/abc303_d
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

INF = 10**18
X, Y, Z = map(int, input().split())
S = input()
N = len(S)

dp = [[INF] * 2 for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = Z

for i in range(N):
    dp[i][0] = min(dp[i][0], dp[i][1]+ Z)
    dp[i][1] = min(dp[i][1], dp[i][0]+ Z)
    if S[i] == 'a':
        dp[i+1][0] = dp[i][0] + X
        dp[i+1][1] = dp[i][1] + Y
    else:
        dp[i+1][0] = dp[i][0] + Y
        dp[i+1][1] = dp[i][1] + X

print(min(dp[N][0], dp[N][1]))
