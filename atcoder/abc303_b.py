# https://atcoder.jp/contests/abc303/tasks/abc303_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]
# print(a, file=sys.stderr)

ok_set = set()
for i in range(M):
    for j in range(N-1):
        ok_set.add(tuple(sorted([a[i][j], a[i][j+1]])))

print(N * (N-1) // 2 - len(ok_set))
