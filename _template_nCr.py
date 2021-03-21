# Template for AtCoder

MOD = 10**9+7

# フェルマーの小定理
def nCr(n, r, mod=MOD):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod
def nPr(n, r, mod=MOD):
    tmp = 1
    for i in range(n, n-r, -1):
        tmp = (tmp * i) % mod
    return tmp

MAXN = 10**5
fact = [1]
ifact = [1]
for i in range(MAXN):
    fact.append(fact[-1] * (i+1) % MOD)
    ifact.append(pow(fact[-1], MOD-2, MOD))
def nCr(n, r):
    return fact[n] * ifact[r] * ifact[n-r] % MOD
def nPr(n, r):
    return fact[n] * ifact[n-r] % MOD
