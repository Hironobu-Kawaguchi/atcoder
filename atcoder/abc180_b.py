# https://atcoder.jp/contests/abc180/tasks/abc180_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
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

N = int(input())
x = list(map(int, (input().split())))
manhattan, euclid, chebyshev = 0, 0, 0
for a in x:
    manhattan += abs(a)
    euclid += a**2
    chebyshev = max(chebyshev, abs(a))
euclid = euclid**0.5
print(manhattan)
print(euclid)
print(chebyshev)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
