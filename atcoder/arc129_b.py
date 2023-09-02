# https://atcoder.jp/contests/arc129/tasks/arc129_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
max_L, min_R = 0, 10**9
for i in range(N):
    L, R = map(int, input().split())
    max_L = max(max_L, L)
    min_R = min(min_R, R)
    if max_L <= min_R:
        print(0)
    else:
        print((max_L - min_R + 1)//2)





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
