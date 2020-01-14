# https://codeforces.com/contest/1288/problem/C

MOD = 10**9+7
f = [1]
for i in range(1020):
    f.append(f[-1]*(i+1)%MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

n, m = map(int, input().split())
ans = nCr(n+2*m-1, 2*m)
print(ans)
