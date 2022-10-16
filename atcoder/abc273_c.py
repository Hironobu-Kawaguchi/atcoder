# https://atcoder.jp/contests/abc273/tasks/abc273_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

N = int(input())
A = list(map(int, (input().split())))

lst = sorted(list(set(A)))
# print(lst)
M = len(lst)

ans = [0]*N
for i in range(N):
    idx = bisect.bisect(lst, A[i])
    ans[M-idx] += 1
for i in range(N):
    print(ans[i])

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
