# https://atcoder.jp/contests/ABC206/tasks/abc206_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from collections import Counter
N = int(input())
A = list(map(int, (input().split())))
cnt = Counter(A)
# print(cnt)
ans = 0
for k, v in cnt.items():
    ans += v*(N-v)

print(ans//2)


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
