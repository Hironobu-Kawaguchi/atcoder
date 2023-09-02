# https://atcoder.jp/contests/abc315/tasks/abc315_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
sf = []
for _ in range(N):
    f, s = map(int, input().split())
    sf.append((s, f))
sf.sort(reverse=True)
ans = 0
flg1, flg2 = False, False
for i in range(1, N):
    if sf[i][1] != sf[0][1] and not flg1:
        flg1 = True
        ans = max(ans, sf[0][0] + sf[i][0])
    elif sf[i][1] == sf[0][1] and not flg2:
        flg2 = True
        ans = max(ans, sf[0][0] + sf[i][0] // 2)
print(ans)
