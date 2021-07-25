# https://atcoder.jp/contests/arc123/tasks/arc123_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
A.sort()
B = list(map(int, (input().split())))
B.sort()
C = list(map(int, (input().split())))
C.sort()

use_B = []
bi = 0
for ai in range(N):
    while B[bi]<=A[ai]:
        bi += 1
        if bi>=N: break
    if bi>=N: break
    use_B.append(B[bi])
    bi += 1
    if bi>=N: break
# print(len(use_B), use_B)

use_C = []
ci = 0
for bi in range(len(use_B)):
    while C[ci]<=use_B[bi]:
        ci += 1
        if ci>=N: break
    if ci>=N: break
    use_C.append(C[ci])
    ci += 1
    if ci>=N: break
# print(len(use_C), use_C)

print(len(use_C))

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
