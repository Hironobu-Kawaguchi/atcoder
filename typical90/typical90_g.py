# https://atcoder.jp/contests/typical90/tasks/typical90_g
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

N = int(input())
A = list(map(int, (input().split())))
A.sort()
Q = int(input())
for qi in range(Q):
    B = int(input())
    i = bisect.bisect_left(A, B)
    if i==0:
        ans = abs(B-A[i])
    elif i==N:
        ans = abs(B-A[i-1])
    else:
        ans = min(abs(B-A[i]), abs(B-A[i-1]))
    print(ans)



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
