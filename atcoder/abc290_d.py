# https://atcoder.jp/contests/abc290/tasks/abc290_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import math

def main():
    N, D, K = map(int, input().split())
    D %= N
    g = math.gcd(N, D)
    q, mod = divmod(K-1, N//g)
    ans = (mod * D + q) % N
    print(ans)

T = int(input())
for ti in range(T):
    main()


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
