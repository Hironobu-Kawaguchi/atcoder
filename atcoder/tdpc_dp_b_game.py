# https://atcoder.jp/contests/tdpc/tasks/tdpc_game

INF = 1001001001
na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0]*(nb+1) for _ in range(na+1)]

for i in range(na, -1, -1):
    for j in range(nb, -1, -1):
        if i==na and j==nb: continue
        if (i+j)&1:
            dp[i][j] = INF
            if i<na: dp[i][j] = min(dp[i+1][j], dp[i][j])
            if j<nb: dp[i][j] = min(dp[i][j+1], dp[i][j])
        else:
            dp[i][j] = 0
            if i<na: dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j])
            if j<nb: dp[i][j] = max(dp[i][j+1] + b[j], dp[i][j])
print(dp[0][0])
