# https://atcoder.jp/contests/abc187/tasks/abc187_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# sys.setrecursionlimit(10 ** 7)
# from itertools import product

import sys
input = sys.stdin.buffer.readline

n = int(input())
x, y = [], []
for i in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        dx = x[j] - x[i]
        if x[i] > x[j]:
            # x, y = y, x
            dx = -dx
        if x[i] < x[j]:
            if (y[j] - y[i]) <= dx and (y[i] - y[j]) <= dx:
                ans += 1
        else:
            if (y[j] - y[i]) <= dx and (y[i] - y[j]) <= dx:
                ans += 1
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
