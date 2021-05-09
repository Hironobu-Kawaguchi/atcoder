# https://atcoder.jp/contests/arc118/tasks/arc118_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import math
t, n = map(int, input().split())
now = (n//t) * (100+t)
rest = n%t
if rest==0:
    while True:
        if math.ceil(now*100/(100+t))*(100+t)//100!=now:
            break
        now -= 1
else:
    while rest>0:
        now += 1
        if math.ceil(now*100/(100+t))*(100+t)//100!=now:
            rest -= 1
print(now)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
