# https://atcoder.jp/contests/abc270/tasks/abc270_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    X, Y, Z = map(int, input().split())
    ans = -1
    if X<0:
        X *= -1; Y *= -1; Z *= -1
    if 0<Y<X:
        if Z<0:
            ans = -2 * Z + X
        elif Z<Y:
            ans = X
    else:
        ans = X        
    print(ans)

main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
