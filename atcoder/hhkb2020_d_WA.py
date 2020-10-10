# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_d
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)

MOD = 10**9+7

# フェルマーの小定理
def nCr(n, r, mod=MOD):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

def main():
    N, A, B = map(int, input().split())
    x = N-A-B
    if x<0:
        print(0)
        return
    ans = (nCr(x+2,2)*2)**2 * ((N-A+1) * (N-B+1) - 1)
    ans %= MOD
    print(ans)
    return

T = int(input())
for t in range(T):
    main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
