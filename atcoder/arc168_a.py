# https://atcoder.jp/contests/arc168/tasks/arc168_a
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from itertools import groupby
N = int(input())
S = input()

ans = 0
for k, g in groupby(S):
    if k == '>':
        m = len(list(g))
        ans += m * (m+1) // 2
print(ans)
