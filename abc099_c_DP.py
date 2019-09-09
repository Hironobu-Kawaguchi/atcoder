# https://atcoder.jp/contests/abc099/tasks/abc099_c
# https://atcoder.jp/contests/abc099/submissions/2645002
N = int(input())
dp = [999999] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    dp[i] = dp[i-1] + 1
    k = 6
    while i - k >= 0:
        dp[i] = min(dp[i], dp[i-k] + 1)
        k *= 6
    k = 9
    while i - k >= 0:
        dp[i] = min(dp[i], dp[i-k] + 1)
        k *= 9
print(dp[N])
