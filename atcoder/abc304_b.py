# https://atcoder.jp/contests/abc304/tasks/abc304_b
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = input()
keta = len(N)
N = int(N)
if keta >= 4:
    N //= 10**(keta-3)
    N *= 10**(keta-3)
print(N)
