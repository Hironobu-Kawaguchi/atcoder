# https://atcoder.jp/contests/abc070/tasks/abc070_c

import fractions
N = int(input())
ans = 1
for i in range(N):
    T = int(input())
    ans = T * ans // fractions.gcd(T, ans)

print(ans)
