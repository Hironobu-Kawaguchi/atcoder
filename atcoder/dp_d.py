# https://atcoder.jp/contests/dp/tasks/dp_d
# pypy
N, W = map(int, input().split())
dp = [-1] * (W+1)
dp[0] = 0

for i in range(N):
    w, v = map(int, input().split())
    for j in range(W-w, -1, -1):
        if dp[j] == -1:
            continue
        else:
            dp[j+w] = max(dp[j+w], dp[j] + v)

print(max(dp))
