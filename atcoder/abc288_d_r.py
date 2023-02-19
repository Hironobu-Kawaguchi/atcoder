# https://atcoder.jp/contests/abc288/tasks/abc288_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, (input().split())))

cum = [[0]*(N+1) for _ in range(K)]
for i in range(N):
    cum[i%K][i+1] = A[i]
for k in range(K):
    for i in range(N):
        cum[k][i+1] += cum[k][i]

Q = int(input())
for qi in range(Q):
    l, r  = map(int, input().split())
    l -= 1
    tst = []
    for k in range(K):
        tst.append(cum[k][r] - cum[k][l])
    tst.sort()
    if tst[0]==tst[-1]:
        print("Yes")
    else:
        print("No")



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
