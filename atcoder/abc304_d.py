# https://atcoder.jp/contests/abc304/tasks/abc304_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import bisect
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())
strawberry = []
for i in range(N):
    p, q = map(int, input().split())
    strawberry.append((p, q))

A = int(input())
a_list = list(map(int, input().split()))
B = int(input())
b_list = list(map(int, input().split()))

cnt = defaultdict(int)
for i in range(N):
    a = bisect.bisect_left(a_list, strawberry[i][0])
    b = bisect.bisect_left(b_list, strawberry[i][1])
    cnt[(a, b)] += 1

m = 10**6 if len(cnt) == (A+1)*(B+1) else 0
M = 0
for k, v in cnt.items():
    m = min(m, v)
    M = max(M, v)
print(m, M)
