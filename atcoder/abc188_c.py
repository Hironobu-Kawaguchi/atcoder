# https://atcoder.jp/contests/abc188/tasks/abc188_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))

mx1 = 0
i1 = 0
for i in range(2**(N-1)):
    if A[i]>mx1:
        mx1 = A[i]
        i1  = i
mx2 = 0
i2 = 0
for i in range(2**(N-1), 2**N):
    if A[i]>mx2:
        mx2 = A[i]
        i2  = i
if mx1>mx2:
    ans = i2 + 1
else:
    ans = i1 + 1
print(ans)


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
