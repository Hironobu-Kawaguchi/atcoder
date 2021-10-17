# https://atcoder.jp/contests/abc223/tasks/abc223_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

N = int(input())
A, B = [], []
for i in range(N):
    _A, _B = map(int, input().split())
    A.append(_A)
    B.append(_B)
T = 0.0
for i in range(N):
    T += A[i] / B[i]
T /= 2
# print(T)
ans = 0.0
for i in range(N):
    tmp = A[i] / B[i]
    if T>tmp:
        ans += A[i]
        T -= tmp
    else:
        ans += B[i] * T
        break
    # print(i, T, ans)
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
