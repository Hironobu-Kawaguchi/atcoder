# https://atcoder.jp/contests/arc154/tasks/arc154_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

N = int(input())
strA = input()
strB = input()
A, B = [], []
for i in range(N):
    if strA[i]<=strB[i]:
        A.append(int(strA[i]))
        B.append(int(strB[i]))
    else:
        A.append(int(strB[i]))
        B.append(int(strA[i]))
# print(A)
# print(B)

moda = 0
keta = 1
for i in range(N-1, -1, -1):
    moda += A[i] * keta
    moda %= MOD
    keta *= 10
    keta %= MOD
modb = 0
keta = 1
for i in range(N-1, -1, -1):
    modb += B[i] * keta
    modb %= MOD
    keta *= 10
    keta %= MOD
ans = moda * modb % MOD
print(ans)


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
