# https://atcoder.jp/contests/abc224/tasks/abc224_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
flg = True
for i1 in range(H-1):
    for i2 in range(i1+1, H):
        for j1 in range(W-1):
            for j2 in range(j1+1, W):
                if A[i1][j1]+A[i2][j2]>A[i2][j1]+A[i1][j2]: flg = False

if flg:
    print("Yes")
else:
    print("No")



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
