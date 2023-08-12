# https://atcoder.jp/contests/abc308/tasks/abc308_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
C = list(input().split())
# print(C)
D = list(input().split())
# print(D)
P = list(map(int, (input().split())))
# print(P)

d = {}
for i in range(M):
    d[D[i]] = P[i+1]
# print(d)

ans = 0
for i in range(N):
    if C[i] in d:
        ans += d[C[i]]
    else:
        ans += P[0]

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
