# https://atcoder.jp/contests/arc126/tasks/arc126_c

import sys
input = sys.stdin.buffer.readline
from math import gcd

N, K = map(int, input().split())
A = list(map(int, (input().split())))

l = A[0]
for i in range(1, N):
    l = gcd(l, A[i])
# print(l)

r = K
for i in range(N):
    r += A[i]
r //= N
# print(r)

def check(now):
    tmp = 0
    for i in range(N):
        mod = A[i] % now
        if mod:
            tmp += now - mod
    if tmp<=K:
        return True
    else:
        return False

while l+1<r:
    now = (l+r)//2
    if check(now):
        l = now
    else:
        r = now

for i in range(60,-1,-1):
    if check(r+i):
        print(r+i)
        break
else:
    print(l)

