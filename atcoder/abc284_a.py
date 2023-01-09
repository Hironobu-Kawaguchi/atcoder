# https://atcoder.jp/contests/ABC284/tasks/abc284_a
# 
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

for i in range(N-1, -1, -1):
    print(S[i])