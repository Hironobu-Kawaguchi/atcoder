# https://atcoder.jp/contests/arc107/tasks/arc107_a
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)
# import math

MOD = 998244353

a, b, c = map(int, input().split())
ans = (a*(a+1) // 2) % MOD
ans *= (b*(b+1) // 2) % MOD
ans *= (c*(c+1) // 2) % MOD
ans %= MOD
print(ans)

# def main():
#     n = int(input())
#     for a in range(1,38):
#         for b in range(1,26):
#             if pow(3,a) + pow(5,b) == n:
#                 print(a, b)
#                 return
#     print(-1)
#     return

# main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
