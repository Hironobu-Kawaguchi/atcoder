# https://atcoder.jp/contests/abc186/tasks/abc186_b
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

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
sumA = 0
minA = 100
for i in range(H):
    for j in range(W):
        sumA += A[i][j]
        minA = min(minA, A[i][j])
ans = sumA - minA*H*W
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
