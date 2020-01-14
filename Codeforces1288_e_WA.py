# https://codeforces.com/contest/1288/problem/E

n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[i+1, i+1, -1] for i in range(n)]

for i in range(m):
    dp[a[i]-1][0] = 1
    if dp[a[i]-1][2] == -1:
        dp[a[i]-1][1] = a[i] + i
    else:
        dp[a[i]-1][1] = min(max(dp[a[i]-1][1], i+1 - dp[a[i]-1][2]), n)
    dp[a[i]-1][2] = i
for i in range(n):
    if dp[i][2] == -1:
        dp[i][1] = n
    else:
        dp[i][1] = min(max(dp[i][1], m - dp[i][2]), n)
    print(dp[i][0], dp[i][1])
