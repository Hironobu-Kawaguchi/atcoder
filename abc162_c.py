# https://atcoder.jp/contests/abc162/tasks/abc162_c

from math import gcd

K = int(input())
ans = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        gcd_ab = gcd(a, b)
        for c in range(1,K+1):
            ans += gcd(gcd_ab, c)
print(ans)
