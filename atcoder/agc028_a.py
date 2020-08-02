# A - Two Abbreviations
# https://atcoder.jp/contests/agc028/tasks/agc028_a
# LCM 最小公倍数 (Least common multiple)
# GCD 最大公約数 (Greatest common divisor)
"""
import fractions

n,m = map(int,input().split())
s = input()
t = input()

g = fractions.gcd(n,m)
l = n*m//g

ng = s[::n//g]
mg = t[::m//g]

if ng == mg:
    print(l)
else:
    print(-1)
"""
from fractions import gcd
N, M = map(int, input().split())
S = input()
T = input()

GCD = gcd(N, M)
LCM = int(N * M / GCD)
flg = True

for i in range(GCD):
    if S[i*N//GCD] == T[i*M//GCD]:
        continue
    else:
        flg = False
if flg:
    print(LCM)
else:
    print(-1)
