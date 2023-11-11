# https://atcoder.jp/contests/abc295/tasks/abc295_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

ans = 0
for k, v in cnt.items():
    ans += v//2

print(ans)
