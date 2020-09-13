# https://atcoder.jp/contests/abc177/tasks/abc178_c

MOD = 10**9+7
n = int(input())

ans = pow(10,n,MOD) - 2 * pow(9,n,MOD) + pow(8,n,MOD)
if ans<0:
    ans += MOD
if ans<0:
    ans += MOD
ans %= MOD
print(ans)