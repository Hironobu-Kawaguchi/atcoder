# https://atcoder.jp/contests/abc152/tasks/abc152_e

from fractions import gcd
MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))

lcm = 1
for a in A:
    lcm *= a//gcd(lcm, a)

print(sum(lcm//a for a in A)%MOD)
