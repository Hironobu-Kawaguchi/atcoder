# https://atcoder.jp/contests/abc185/tasks/abc185_e

N, M = map(int, input().split())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))

INF = 1001001001001
dp = [[INF] * (M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N+1):
    for j in range(M+1):
        if i<N: dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
        if j<M: dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
        if i<N and j<M:
            if A[i] == B[j]: co = 0
            else:            co = 1
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+co)
print(dp[N][M])
