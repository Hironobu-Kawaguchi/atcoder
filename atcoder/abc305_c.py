# https://atcoder.jp/contests/abc305/tasks/abc305_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
iset, jset = set(), set()
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            iset.add(i)
            jset.add(j)
for i in range(H):
    for j in range(W):
        if S[i][j]=='.' and i in iset and j in jset:
            print(i+1, j+1)
            exit()


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
