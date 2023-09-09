# https://atcoder.jp/contests/abc318/tasks/abc318_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
size = 100
hex = [[False]*size for _ in range(size)]
for i in range(N):
    a, b, c, d = map(int, input().split())
    for x in range(a, b):
        for y in range(c, d):
            hex[x][y] = True
ans = 0
for i in range(size):
    for j in range(size):
        if hex[i][j]: ans += 1
print(ans)
