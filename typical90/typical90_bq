# https://atcoder.jp/contests/typical90/tasks/typical90_bq
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 1000000007

N, K = map(int, input().split())
ans = 1
if N==1:
    ans = K
elif N==2:
    ans = K * (K-1)
else:
    ans = K * (K-1) * pow(K-2, N-2, MOD)
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
