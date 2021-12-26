# https://atcoder.jp/contests/typical90/tasks/typical90_r
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for qi in range(Q):
    E = int(input())
    y = -math.cos(math.pi * (2*E/T - 0.5)) * L / 2
    z = math.sin(math.pi * (2*E/T - 0.5)) * L / 2 + L / 2
    theta = math.atan2(z ,math.sqrt(X**2+(Y-y)**2))
    # print(y, z)
    print(theta*180/math.pi)



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
