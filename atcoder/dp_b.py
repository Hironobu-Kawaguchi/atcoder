# https://atcoder.jp/contests/dp/tasks/dp_b

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * N
for i in range(1, N):
    dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    for j in range(2, K+1):
        if i-j < 0:
            break
        dp[i] = min(dp[i], dp[i-j] + abs(h[i]-h[i-j]))

# print(dp)
print(dp[-1])
