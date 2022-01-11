# https://atcoder.jp/contests/typical90/tasks/typical90_bl
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
A = list(map(int, input().split()))
diff = []
ans = 0
for i in range(N-1):
    diff.append(A[i+1] - A[i])
    ans += abs(diff[i])
for i in range(Q):
    L, R, V = map(int, input().split())
    if L!=1:
        ans += abs(diff[L-2] + V) - abs(diff[L-2])
        diff[L-2] += V
    if R!=N:
        ans += abs(diff[R-1] - V) - abs(diff[R-1])
        diff[R-1] -= V
    print(ans)

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
