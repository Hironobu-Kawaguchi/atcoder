# https://atcoder.jp/contests/abc177/tasks/abc178_d

MOD = 10**9+7

MAXN = 2000
fact = [1]
ifact = [1]
for i in range(MAXN):
    fact.append(fact[-1] * (i+1) % MOD)
    ifact.append(pow(fact[-1], MOD-2, MOD))
def nCr(n, r):
    return fact[n] * ifact[r] * ifact[n-r] % MOD
def nPr(n, r):
    return fact[n] * ifact[n-r] % MOD

s = int(input())
n = s//3

ans = 0
for i in range(1,n+1):
    r = s - 3*i
    ans += nCr(r+i-1, i-1)
ans %= MOD
print(ans)