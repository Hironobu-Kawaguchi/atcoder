# https://atcoder.jp/contests/typical90/tasks/typical90_ca
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
B = [[int(i) for i in input().split()] for _ in range(H)]

cnt = 0
for x in range(H-1):
    for y in range(W-1):
        dif = B[x][y] - A[x][y]
        A[x][y] += dif
        A[x+1][y] += dif
        A[x][y+1] += dif
        A[x+1][y+1] += dif
        cnt += abs(dif)
flg = True
for x in range(H):
    if A[x][W-1]!=B[x][W-1]:
        flg = False
for y in range(W):
    if A[H-1][y]!=B[H-1][y]:
        flg = False

if flg:
    print("Yes")
    print(cnt)
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
