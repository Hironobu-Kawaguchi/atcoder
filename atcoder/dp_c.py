# https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
dp = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())
    x = max(dp[1] + a, dp[2] + a)
    y = max(dp[2] + b, dp[0] + b)
    z = max(dp[0] + c, dp[1] + c)
    dp = [x, y, z]

print(max(dp))
