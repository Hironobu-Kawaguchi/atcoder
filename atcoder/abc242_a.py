# https://atcoder.jp/contests/abc242/tasks/abc242_a
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

A, B, C, X = map(int, input().split())
ans = 0.0
if X<=A:
    ans = 1.0
elif X>B:
    ans = 0.0
else:
    ans = C/(B-A)
print(ans)


# main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
