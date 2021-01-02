# https://atcoder.jp/contests/abc187/tasks/abc187_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# sys.setrecursionlimit(10 ** 7)
# from itertools import product

# import sys
# input = sys.stdin.buffer.readline
from collections import defaultdict

n = int(input())
d = defaultdict(int)
for i in range(n):
    s = input()
    if s[0] == '!':
        d[s[1:]] |= 1
    else:
        d[s] |= 2
ans = 'satisfiable'
for k,v in d.items():
    if v==3:
        ans = k
        break
print(ans)

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
