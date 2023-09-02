# https://atcoder.jp/contests/abc219/tasks/abc219_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
INF = 1001001001

N = int(input())
X, Y = map(int, input().split())
ab = []
for _ in range(N):
    a, b = map(int, input().split())
    ab.append((a, b))

dp = [[[INF for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for x in range(X+1):
        for y in range(Y+1):
            if dp[i][x][y] == INF:
                continue
            dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])
            nx = min(x + ab[i][0], X)
            ny = min(y + ab[i][1], Y)
            dp[i+1][nx][ny] = min(dp[i+1][nx][ny], dp[i][x][y] + 1)

# print(dp, file=sys.stderr)
if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
