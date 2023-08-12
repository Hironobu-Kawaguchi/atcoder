# https://atcoder.jp/contests/abc310/tasks/abc310_e
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H, W, N = map(int, input().split())
grid = [[True]*(W+1) for _ in range(H+1)]
for i in range(N):
    a, b = map(int, input().split())
    grid[a][b] = False

dp = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        if grid[i+1][j+1] and dp[i+1][j] and grid[i][j+1]:
            dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        elif grid[i+1][j+1]:
            dp[i+1][j+1] = 1
ans = 0
for i in range(H+1):
    # print(dp[i], file=sys.stderr)
    for j in range(W+1):
        ans += dp[i][j]
print(ans)
