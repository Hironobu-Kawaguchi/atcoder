# https://atcoder.jp/contests/abc142/tasks/abc142_d

import math

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x%y)

def factorize(n):
    res = []
    for i in range(2, int(math.sqrt(n))+1):
        if n%i: continue
        res.append([i,0])
        while n%i == 0:
            n /= i
            res[-1][1] += 1
    if n != 1: res.append([n,1])
    return res

a, b = map(int, input().split())
g = gcd(a,b)
f = factorize(g)
ans = len(f) + 1
print(ans)
