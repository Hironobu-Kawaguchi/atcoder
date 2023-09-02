# https://atcoder.jp/contests/abc315/tasks/abc315_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

M = int(input())
D = list(map(int, input().split()))
all_days = sum(D)
middle_days = (all_days + 1) // 2
for a in range(M):
    if D[a] < middle_days:
        middle_days -= D[a]
    else:
        b = middle_days
        a += 1
        break
print(a, b)
