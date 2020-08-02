# https://atcoder.jp/contests/abc172/tasks/abc172_e
# 攪乱順列（完全順列）　包除原理

MOD = 10**9+7
MAXN = 5*(10**5)+5
fact = [1]
ifact = [1]
for i in range(MAXN):
    fact.append(fact[-1] * (i+1) % MOD)
    ifact.append(pow(fact[-1], MOD-2, MOD))
def nCr(n, r):
    return fact[n] * ifact[r] * ifact[n-r] % MOD

def nPr(n, r):
    return fact[n] * ifact[n-r] % MOD

n, m = map(int, input().split())
ans = 0
for k in range(n+1):
    # tmp = pow(nPr(m-k, n-k), 2, MOD) * nPr(m, k) * nCr(n,k) % MOD
    # tmp = nPr(m-k, n-k) * nPr(m, n) * nCr(n,k) % MOD
    tmp = nPr(m-k, n-k) * nCr(n,k) % MOD
    if k%2:
        ans -= tmp
    else:
        ans += tmp
ans = (ans * nPr(m, n) + MOD) % MOD
print(ans)
