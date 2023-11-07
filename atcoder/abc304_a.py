# https://atcoder.jp/contests/abc304/tasks/abc304_a
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S, A = [], []
for _ in range(N):
    s, a = input().split()
    S.append(s)
    A.append(int(a))

minA, minIdx = 1001001001, -1
for i in range(N):
    if A[i] < minA:
        minA = A[i]
        minIdx = i
for i in range(N):
    now = (i + minIdx) % N
    print(S[now])
