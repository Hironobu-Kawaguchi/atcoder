# https://atcoder.jp/contests/abc034/tasks/abc034_c

MOD = 1000000007
W, H = map(int, input().split())
dp = [[0] * (H+1) for _ in range(W+1)]
dp[1][0] = 1

for i in range(1, W+1):
    for j in range(1, H+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[W][H])
