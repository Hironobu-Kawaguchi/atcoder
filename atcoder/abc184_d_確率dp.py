# https://atcoder.jp/contests/abc184/tasks/abc184_d

a, b, c = map(int, input().split())
dp = [[[0]*101 for j in range(101)]*101 for i in range(101)]
for i in range(99,-1,-1):
    for j in range(99,-1,-1):
        for k in range(99,-1,-1):
            if i+j+k==0: continue
            now = 0
            now += dp[i+1][j][k] * i
            now += dp[i][j+1][k] * j
            now += dp[i][j][k+1] * k
            dp[i][j][k] = now/(i+j+k) + 1

print(dp[a][b][c])
