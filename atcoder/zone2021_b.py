# https://atcoder.jp/contests/zone2021/tasks/zone2021_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

n, d, h = map(int, input().split())
ans = 0.0
for i in range(n):
    _d, _h = map(int, input().split())
    h0 = h - d * (h-_h) / (d-_d)
    ans = max(ans, h0)
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
