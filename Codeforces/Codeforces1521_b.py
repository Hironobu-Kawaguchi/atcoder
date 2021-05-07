# https://codeforces.com/contest/1521/problem/A

from math import gcd

def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    ans = []
    mina = 10**9 + 1
    i = 0
    for j in range(n):
        if a[j]<mina:
            i = j
            mina = a[j]
    now = 10**9 + 1
    for j in range(i-1,-1,-1):
        if gcd(a[j+1], a[j])==1:
            continue
        while gcd(a[j+1], now)!=1:
            now += 1
        a[j] = now
        ans.append((i+1, j+1, a[i], a[j]))
        k += 1
        if gcd(a[j+1], a[j])!=1:
            print("Error", j, a[j+1], a[j], gcd(a[j+1], a[j]))
        assert gcd(a[j+1], a[j])==1
    now = 10**9 + 1
    for j in range(i+1,n):
        if gcd(a[j-1], a[j])==1:
            continue
        while gcd(a[j-1], now)!=1:
            now += 1
        a[j] = now
        ans.append((i+1, j+1, a[i], a[j]))
        k += 1
        if gcd(a[j-1], a[j])!=1:
            print("Error", j, a[j-1], a[j], gcd(a[j-1], a[j]))
        assert gcd(a[j-1], a[j])==1
    print(k)
    assert k<=n
    for i in range(k):
        print(*ans[i])
    return

t = int (input())
for _ in range(t):
    main()
