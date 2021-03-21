# https://atcoder.jp/contests/abc188/tasks/abc188_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))
ans = 0
for i in range(N):
    ans += A[i]*B[i]
if ans==0:
    print("Yes")
else:
    print("No")

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
