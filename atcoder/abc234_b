# https://atcoder.jp/contests/ABC234/tasks/abc234_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
x, y = [], []
for i in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)
ans = 0
for i in range(N):
    for j in range(N):
        ans = max((x[i]-x[j])**2 + (y[i]-y[j])**2, ans)

print(ans**0.5)



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
