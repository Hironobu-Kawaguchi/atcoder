# https://atcoder.jp/contests/newjudge-2308-algorithm/tasks/abc273_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

X, K = map(int, input().split())
pow10 = 1
for i in range(K):
    X //= pow10
    m = X % 10
    if m < 5: X -= m
    else: X += 10 - m
    X *= pow10
    pow10 *= 10
print(X)



# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
