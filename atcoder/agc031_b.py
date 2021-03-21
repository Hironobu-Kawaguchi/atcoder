# https://atcoder.jp/contests/agc031/tasks/agc031_b

N = int(input())
C = [int(input()) for _ in range(N)]

dp = [0] * N
dp[0] = 1
d = {C[0]:0}

for i in range(1, N):
    if C[i] in d and C[i] != C[i-1]:
        dp[i] = (dp[i-1] + dp[d[C[i]]]) % (10**9+7)
    else:
        dp[i] = dp[i-1]
    d[C[i]] = i

print(dp[-1])
