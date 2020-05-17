# https://atcoder.jp/contests/abc168/tasks/abc168_e

import sys
from math import gcd
from collections import Counter
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 1000000007

N = int(input())
ab = []
for i in range(N):
    a,b = map(int, input().split())
    gcd_ab = gcd(a,b)
    a //= gcd_ab
    b //= gcd_ab
    if a<0:     # aは常に正にする
        a *= -1
        b *= -1
    ab.append((a,b))
Cnt = Counter(ab)
# print(Cnt)

ans = 1
done = set()
for (a, b), c in Cnt.items():
    # print(a,b,c)
    if (a,b) in done: continue
    if (a,b) == (0,0):
        done.add((a,b))
        continue
    elif b < 0:
        if (-b, a) in Cnt.keys():
            ans *= (pow(2,c,MOD)-1) + (pow(2,Cnt[(-b,a)],MOD)-1) + 1
            ans %= MOD
            done.add((a,b))
            done.add((-b,a))
        else:
            ans *= pow(2,c,MOD)
            ans %= MOD
            done.add((a,b))
    else:
        if (b, -a) in Cnt.keys():
            ans *= (pow(2,c,MOD)-1) + (pow(2,Cnt[(b,-a)],MOD)-1) + 1
            ans %= MOD
            done.add((a,b))
            done.add((b,-a))
        else:
            ans *= pow(2,c,MOD)
            ans %= MOD
            done.add((a,b))
# print(done)
if (0,0) not in Cnt:
    ans -= 1
    ans % MOD
print(ans)

# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
