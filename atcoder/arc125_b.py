# https://atcoder.jp/contests/arc125/tasks/arc125_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import math
MOD = 998244353
N = int(input())
sqN = int(math.sqrt(N))
# print(sqN)
ans = 0
for minus in range(1, sqN+1):
    max_plus = N//minus
    # print(max_plus)
    ans += (max_plus + 2 - minus)//2
    # if max_plus<=2:
    #     ans += max_plus
    # else:
    #     ans += (max_plus - 1) * (max_plus - 2) // 2 + 2
    ans %= MOD
print(ans)



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
