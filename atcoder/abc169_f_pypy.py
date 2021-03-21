# https://atcoder.jp/contests/abc169/tasks/abc169_f

import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N, S = map(int, input().split())
A = list(map(int, (input().split())))
dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(S+1):
        dp[i+1][j] += dp[i][j]*2
        dp[i+1][j] %= MOD
        if j+A[i] <= S:
            dp[i+1][j+A[i]] += dp[i][j]
            dp[i+1][j+A[i]] %= MOD
print(dp[-1][S])

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
