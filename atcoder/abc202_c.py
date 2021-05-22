# https://atcoder.jp/contests/abc202/tasks/abc202_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
B = list(map(int, (input().split())))
C = list(map(int, (input().split())))

CntA = [0]*(N+1)
CntB = [0]*(N+1)
for i in range(N):
    CntA[A[i]] += 1
for j in range(N):
    CntB[B[C[j]-1]] += 1

ans = 0
for i in range(N+1):
    ans += CntA[i]*CntB[i]
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
