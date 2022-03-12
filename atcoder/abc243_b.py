# https://atcoder.jp/contests/abc243/tasks/abc243_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import Counter

N = int(input())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))

ans1 = 0
for i in range(N):
    if A[i]==B[i]:
        ans1 += 1
ans2 = 0
cntA = Counter(A)
cntB = Counter(B)
for k, v in cntA.items():
    if k in cntB:
        ans2 += v * cntB[k]
print(ans1)
print(ans2-ans1)


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
