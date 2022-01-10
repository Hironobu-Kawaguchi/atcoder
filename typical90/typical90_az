# https://atcoder.jp/contests/typical90/tasks/typical90_az
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 10**9+7

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for i in range(N):
    tmp = 0
    for j in range(6):
        tmp += A[i][j]
    ans *= tmp
    ans %= MOD
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
