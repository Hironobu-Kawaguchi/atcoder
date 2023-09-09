# https://atcoder.jp/contests/abc318/tasks/abc318_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M, P = map(int, input().split())
ans = 0
for i in range(M, N+1):
    if (i-M)%P==0:
        ans += 1
print(ans)
