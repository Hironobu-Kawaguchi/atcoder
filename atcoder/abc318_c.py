# https://atcoder.jp/contests/abc318/tasks/abc318_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
ans = 0
for i in range((N+D-1)//D):
    tmp = 0
    for j in range(D):
        if i*D+j >= N: break
        tmp += F[i*D+j]
    if tmp > P:
        ans += P
    else:
        ans += tmp
print(ans)

