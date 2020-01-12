# https://atcoder.jp/contests/abc151/tasks/abc151_e

mod = 10**9+7
f = [1]
for i in range(10**5+7):
    f.append(f[-1]*(i+1)%mod)
def comb(n, r,mod=mod):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(n-k+1):
    ans += (a[i] - a[-1-i]) * comb(n-1-i, k-1)
    ans %= mod
print(ans)
