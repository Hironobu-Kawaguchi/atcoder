# https://atcoder.jp/contests/abc180/tasks/abc180_e
# bitDP

INF = 1001001001
n = int(input())
xyz = [[int(i) for i in input().split()] for _ in range(n)]
dist = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = abs(xyz[j][0]-xyz[i][0]) + abs(xyz[i][1]-xyz[j][1]) + max(0, xyz[j][2]-xyz[i][2])
n2 = 1<<n
dp = [[INF]*n for _ in range(n2)]
for i in range(n):
    if i==0: continue
    dp[1<<i][i] = dist[0][i]
for i in range(n2):
    for j in range(n):
        if not (i>>j&1): continue
        for k in range(n):
            if (i>>k&1): continue
            dp[i|1<<k][k] = min(dp[i|1<<k][k], dp[i][j] + dist[j][k])
print(dp[n2-1][0])
