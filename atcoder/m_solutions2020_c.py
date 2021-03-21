# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, (input().split())))

for i in range(N-K):
    if A[i+K] > A[i]:
        print("Yes")
    else:
        print("No")


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
