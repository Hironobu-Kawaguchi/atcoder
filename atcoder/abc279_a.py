# https://atcoder.jp/contests/ABC279/tasks/abc279_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

S = input()
ans = 0
for c in S:
    if c=='v': ans += 1
    elif c=='w': ans += 2
print(ans)


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
