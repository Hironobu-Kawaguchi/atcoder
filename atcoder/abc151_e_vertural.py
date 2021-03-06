# https://atcoder.jp/contests/abc151/tasks/abc151_e

MOD = 10**9+7
f = [1]
for i in range(10**5):
    f.append(f[-1] * (i+1) % MOD)

def nCr(n,r,mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N-K+1):
    ans += (A[-i-1] - A[i]) * nCr(N-1-i, K-1)
    ans %= MOD
print(ans)
