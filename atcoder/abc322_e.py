# https://atcoder.jp/contests/abc322/tasks/abc322_e

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18

N, K, P = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [dict() for _ in range(N+1)]
for k in range(K):
    dp[0] = {tuple([0] * K): 0}
# print(dp[0], file=sys.stderr)

for i in range(N):
    for k, v in dp[i].items():
        if dp[i+1].get(k) is None:
            dp[i+1][k] = v
        else:
            dp[i+1][k] = min(dp[i+1][k], v)
        k = list(k)
        cost = A[i][0]
        for j in range(K):
            k[j] += A[i][j+1]
            k[j] = min(k[j], P)
        k = tuple(k)
        if dp[i+1].get(k) is None:
            dp[i+1][k] = v + cost
        else:
            dp[i+1][k] = min(dp[i+1][k], v + cost)

fill = tuple([P] * K)
if dp[N].get(fill) is None:
    print(-1)
else:
    print(dp[N][fill])
