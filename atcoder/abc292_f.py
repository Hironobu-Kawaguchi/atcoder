# https://atcoder.jp/contests/abc292/tasks/abc292_f
# from numba import njit
# from functools import lru_cache


import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import math

A, B = map(int, input().split())
if A<B:
    A, B = B, A
l = B
# r = (B*B + A*A)**0.5
r = B / math.cos(math.pi / 6)

while r>l+1e-10:
    x = (r+l)/2
    deg = math.acos(B/x)
    # if deg>=math.pi/6:
    #     r = x
    #     continue
    # print(deg)
    y = x * math.sin(deg + math.pi/3)
    # print(x, y)
    if y>A:
        r = x
    else:
        l = x
print(l)
