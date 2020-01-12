# https://atcoder.jp/contests/abc151/tasks/abc151_e

MOD = 10**9+7
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)

factorial = [0] * (N+2)

def fact(n, MOD=MOD):
    global factorial
    if n == 0:
        factorial[n] = 1
        return 1
    res = n * fact(n-1)
    res %= MOD
    factorial[n] = res
    return res

fact(N+1)
# print(fact(N, MOD))
# print(factorial)

def nCr(n, r, mod=10**9+7):
    res = factorial[n]
    res //= factorial[r]
    res //= factorial[n-r]
    res %= MOD
    return res

# # フェルマーの小定理
# def nCr(n, r, mod=10**9+7):
#     r = min(r, n-r)
#     numer = denom = 1
#     for i in range(1, r+1):
#         numer = numer * (n+1-i) % mod
#         denom = denom * i % mod
#     return numer * pow(denom, mod-2, mod) % mod

ans = 0
for i in range(K+1):
    c = nCr(i+K-1, i)
    ans += c * A[N-K-1+i]
    ans -= c * A[K-i]
    ans %= MOD
ans %= MOD
print(ans)
