# https://atcoder.jp/contests/abc156/tasks/abc156_d

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9+7

def nCr(n, r, mod=MOD):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

n, a, b = map(int, (input().split()))

ans = pow(2, n, MOD) - 1 - nCr(n, a) - nCr(n, b)
ans += MOD * 2
ans %= MOD
print(ans)
