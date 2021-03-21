# https://atcoder.jp/contests/abc147/tasks/abc147_d

N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

ans = 0
for i in range(60):
    ones = 0
    for j in range(N):
        if ((A[j] >> i) & 1):
            ones += 1
    ans += 2**i * ones * (N - ones) % MOD
    ans %= MOD

print(ans)
