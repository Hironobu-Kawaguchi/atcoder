# https://atcoder.jp/contests/abc034/tasks/abc034_c

W, H = map(int, input().split())

def nCr(n, r, mod=10**9+7):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

print(nCr(W+H-2, W-1))
