import sys
input = sys.stdin.readline

INF = 10**18

def solve(q):
    E, W = map(int, input().split())
    weights = [list(map(int, input().split())) for _ in range(E)]
    cp = [[0] * (E+1) for _ in range(E)]
    for i in range(E):
        minw = [INF] * W
        for j in range(i, E):
            for k in range(W):
                minw[k] = min(minw[k], weights[j][k])
            cp[i][j+1] = sum(minw)
    dp = [[INF] * (E+1) for _ in range(E)]
    for i in range(E):
        dp[i][i+1] = 2*cp[i][i+1]
    for l in range(2, E+1):
        for i in range(E-l+1):
            j = i + l
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] - 2*cp[i][j])
    print(f"Case #{q}: {dp[0][E]}")

T = int(input())
for t in range(T):
    solve(t+1)