# https://atcoder.jp/contests/abc276/tasks/abc276_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import math

N = int(input())
A = list(map(int, (input().split())))

gcd = A[0]
for i in range(N-1):
    gcd = math.gcd(gcd, A[i+1])
for i in range(N):
    A[i] //= gcd
# print(gcd)

ans = 0
for i in range(N):
    while A[i]>1:
        if A[i]%2==0:
            A[i] //= 2
            ans += 1
        elif A[i]%3==0:
            A[i] //= 3
            ans += 1
        else:
            ans = -1
            break
        # print(A[i])
    if ans==-1:
        break
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
