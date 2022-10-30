# https://atcoder.jp/contests/abc275/tasks/abc275_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import copy
MOD = 998244353

N, M, K = map(int, input().split())

# x = 1
y = [0] * (N+1)
y[0] = 1
m_inv = pow(M, MOD-2, MOD)
for k in range(K):
    next_y = [0] * (N+1)
    # x *= M
    next_y[N] += y[N]
    for i in range(N):
        for j in range(1, M+1):
            now = i+j
            if i+j>N: now = N - (i+j-N)
            next_y[now] += y[i] * m_inv
            next_y[now] %= MOD
    y = copy.copy(next_y)
# print(pow(M, K, MOD), y[N])
# print(y)

ans = y[N]
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
