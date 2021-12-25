# https://atcoder.jp/contests/typical90/tasks/typical90_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
hsum = [0]*H
for i in range(H):
    tmp = 0
    for j in range(W):
        tmp += A[i][j]
    hsum[i] = tmp
wsum = [0]*W
for j in range(W):
    tmp = 0
    for i in range(H):
        tmp += A[i][j]
    wsum[j] = tmp
B = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j] = hsum[i] + wsum[j] - A[i][j]
for i in range(H):
    print(*B[i])



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
