# https://atcoder.jp/contests/arc106/tasks/arc106_d

MOD = 998244353

# フェルマーの小定理
def nCr(n, r, mod=MOD):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


def main():
    N, K = map(int, input().split())
    A = list(map(int, (input().split())))
    sumAs = []
    fact = [1]
    for i in range(K):
        fact.append(fact[-1] * (i+1) % MOD)
    for k in range(K+1):
        tmp = 0
        for i in range(N):
            tmp += pow(A[i], k, MOD)
        tmp //= fact[k]
        sumAs.append(tmp)

    sums = []
    for k in range(K+1):
        tmp = 0
        for i in range(N):
            tmp += pow(A[i], K-k, MOD)
        tmp //= fact[K-k]
        sums.append(sumAs[k] * tmp % MOD)
    
    tmp = 0
    for X in range(1,K+1):
        tmp += sums[X]
        ans = fact[X] * tmp
        ii = 0
        for i in range(N):
            ii += pow(A[i]*2, X, MOD)
        ii %= MOD
        ans -= ii
        ans //= 2
        print(ans)
    return

main()
