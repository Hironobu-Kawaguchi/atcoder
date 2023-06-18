# https://atcoder.jp/contests/arc159/tasks/arc159_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from math import gcd

def main():
    A, B = map(int, input().split())
    if A==B:
        print(1)
        return
    if A<B:
        A, B = B, A
    ans = [0]

    # def gcd(a, b):
    #     ans[0] += 1
    #     return gcd(b, a % b) if b else a
    
    # gcd(A, B)
    # print(ans[0])

    g = gcd(A, B)
    ans = 0
    while A-B!=g and B>0:
        y = (A-B)//g
        factorization = set()
        for i in range(1, int(y**0.5)+1):
            if y%i==0:
                factorization.add(i)
                factorization.add(y//i)
        factorization = list(factorization)
        # print(factorization)
        x = 1001001001001001001
        for f in factorization:
            if A % (g*f):
                x = min(x, (A % (g*f)) // g)
        # if x==0:
        #     x = 1
        # print(x, g)
        A -= g * x
        B -= g * x
        g = gcd(A, B)
        ans += x
        # print(g, A, B, ans)
    ans += B // g
    print(ans)
    return

main()
