# C - GCD on Blackboard
# https://atcoder.jp/contests/abc125/tasks/abc125_c

from fractions import gcd
N = int(input())
A = list(map(int, input().split()))

gcd_l = [0]
gcd_r = [0]
for i in range(N):
    gcd_l.append(gcd(gcd_l[i], A[i]))
    gcd_r.append(gcd(gcd_r[i], A[-(i+1)]))

gcds = []
for i in range(N):
    gcds.append(gcd(gcd_l[i], gcd_r[-(i+2)]))
ans = max(gcds)
print(ans)

"""
N = int(input())
AA = list(map(int, input().split()))

l = []
for i in range(N):
    A = AA.copy()
    A.pop(i)
    minA = min(A)
    while len(A) > 1:
        minA = min(A)
        tempA = []
        tempA.append(minA)
        for a in A:
            mod = a % minA
            if mod > 0:
                tempA.append(mod)
        A = tempA
    l.append(A[0])
# print(l)
print(max(l))
"""