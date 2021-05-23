# https://atcoder.jp/contests/arc120/tasks/arc120_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
max_A = [0] * (N+1)
cum_A = [0] * (N+1)
cum_cum_A = [0] * (N+1)

max_temp = 0
for i in range(N):
    max_A[i+1] = max(max_A[i], A[i])
    cum_A[i+1] = cum_A[i] + A[i]
    cum_cum_A[i+1] = cum_cum_A[i] + cum_A[i+1]

for i in range(N):
    print(cum_cum_A[i+1] + max_A[i+1]*(i+1))

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
