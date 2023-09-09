# https://atcoder.jp/contests/abc318/tasks/abc318_e
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))
d = {}
for i in range(N):
    if A[i] not in d: d[A[i]] = []
    d[A[i]].append(i)
# print(d, file=sys.stderr)

ans = 0
for k, v in d.items():
    if len(v)==1: continue
    # for i in range(len(v)-1):
    #     for j in range(i+1, len(v)):
    #         ans += v[j] - v[i] - (j-i)
    for i in range(len(v)-1):
        diff_cnt = v[i+1] - v[i] - 1
        ans += diff_cnt * (i+1) * (len(v)-i-1)
print(ans)
