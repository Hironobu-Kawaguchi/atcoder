# https://atcoder.jp/contests/dp/tasks/dp_e

N, W = map(int, input().split())
dp = [10000000001] * (10**3 * N + 1)
dp[0] = 0

for i in range(N):
    w, v = map(int, input().split())
    for j in range(len(dp)-1, v-1, -1):
        if dp[j-v] + w <= W:
            dp[j] = min(dp[j-v] + w, dp[j])

for j in range(len(dp)-1, v-1, -1):
    if dp[j] <= W:
        ans = j
        break

print(ans)
