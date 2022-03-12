# https://atcoder.jp/contests/typical90/tasks/typical90_ar
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
A = list(map(int, (input().split())))
z = 0
for qi in range(Q):
    T, x, y = map(int, input().split())
    if T==1:
        A[(x-1-z)%N], A[(y-1-z)%N] = A[(y-1-z)%N], A[(x-1-z)%N]
    elif T==2:
        z += 1
    else:
        print(A[(x-1-z)%N])


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
