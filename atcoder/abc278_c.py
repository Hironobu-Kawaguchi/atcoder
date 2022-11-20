# https://atcoder.jp/contests/abc278/tasks/abc278_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

d = defaultdict(set)
N, Q = map(int, input().split())
for qi in range(Q):
    t, a, b = map(int, input().split())
    if t==1:
        d[a].add(b)
    elif t==2:
        if b in d[a]:
            d[a].remove(b)
    else:
        if ((a in d[b]) and (b in d[a])):
            print("Yes")
        else:
            print("No")



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
