# https://atcoder.jp/contests/abc314/tasks/abc314_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

N = int(input())
print(pi[:N+2])
