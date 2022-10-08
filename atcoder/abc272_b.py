# https://atcoder.jp/contests/abc271/tasks/abc272_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
chk = [set() for _ in range(N)]
for i in range(M):
    x = list(map(int, input().split()))
    # print(x, x[0]+2)
    for j in range(1, x[0]+1):
        chk[x[j]-1] |= set(x[1:])
    # print(chk)
ans = 'Yes'
for i in range(N):
    if len(chk[i])<N:
        ans = 'No'
print(ans)
