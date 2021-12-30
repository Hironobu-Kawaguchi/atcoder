# https://atcoder.jp/contests/typical90/tasks/typical90_at
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
cntA, cntB, cntC = [0]*46, [0]*46, [0]*46
for i in range(N):
    cntA[A[i]%46] += 1
    cntB[B[i]%46] += 1
    cntC[C[i]%46] += 1
cntAB = [0]*46
for i in range(46):
    for j in range(46):
        cntAB[(i+j)%46] += cntA[i]*cntB[j]
cntABC = [0]*46
for i in range(46):
    for j in range(46):
        cntABC[(i+j)%46] += cntAB[i]*cntC[j]
print(cntABC[0])


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
