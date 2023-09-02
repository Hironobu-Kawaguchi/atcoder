# https://atcoder.jp/contests/arc154/tasks/arc154_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353
N = int(input())
A = list(input())
B = list(input())
for i in range(N):
    if A[i]>B[i]:
        A[i], B[i] = B[i], A[i]
Aint = int("".join(A)) % MOD
Bint = int("".join(B)) % MOD
print(Aint * Bint % MOD)


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
