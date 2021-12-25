# https://atcoder.jp/contests/typical90/tasks/typical90_j
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A, B = [0]*N, [0]*N
for i in range(N):
    C, P = map(int, input().split())
    if C==1:
        A[i] = P
    else:
        B[i] = P
cumA, cumB = [0], [0]
for i in range(N):
    cumA.append(cumA[-1]+A[i])
    cumB.append(cumB[-1]+B[i])
# print(cumA)
# print(cumB)

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    print(cumA[R]-cumA[L-1], cumB[R]-cumB[L-1])


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
