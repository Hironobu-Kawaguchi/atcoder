# https://atcoder.jp/contests/abc150/tasks/abc150_d

import fractions
import sys
readline = sys.stdin.buffer.readline
N, M = map(int, readline().split())
a = list(map(int, readline().split()))
# print(N, M, a)

MOD = 10**9 + 7

tmp = 1
for x in a:
    x //= 2
    tmp2 = x // fractions.gcd(tmp, x)
    M //= tmp2
    tmp *= tmp2
    tmp %= MOD

ans = (M + 1) // 2
print(ans)

