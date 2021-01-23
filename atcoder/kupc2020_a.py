# https://atcoder.jp/contests/kupc2020/tasks/kupc2020_a
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
for i in range(N-1):
    ans += abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
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
