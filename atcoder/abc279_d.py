# https://atcoder.jp/contests/ABC279/tasks/abc279_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())

def f(x):
    return A / (1+x)**0.5 + B*x

l, r = 0, 10**36
while l+1<r:
    now = (l+r)//2
    if f(now)>f(now+1):
        l = now
    else:
        r = now
fl, fr = f(l), f(r)
if fl>fr:
    # print(l)
    print(fr)
else:
    # print(r)
    print(fl)


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
