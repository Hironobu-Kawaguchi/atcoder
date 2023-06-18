# https://atcoder.jp/contests/abc293/tasks/abc293_c
# from numba import njit
# from functools import lru_cache


import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]

dp = [[[] for _ in range(W)] for _ in range(H)]
dp[0][0].append(set([A[0][0]]))
# print(dp)
for i in range(H):
    for j in range(W):
        if i<H-1:
            for st in dp[i][j]:
                if A[i+1][j] in st: continue
                dp[i+1][j].append(st | set([A[i+1][j]]))
        if j<W-1:
            for st in dp[i][j]:
                if A[i][j+1] in st: continue
                dp[i][j+1].append(st | set([A[i][j+1]]))
print(len(dp[H-1][W-1]))


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
