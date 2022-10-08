# https://atcoder.jp/contests/abc271/tasks/abc271_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
a = list(map(int, input().split()))
vol = [False] * (N+2)
sold = 0
for i in range(N):
    if a[i]>N:
        sold += 1
    elif vol[a[i]]:
        sold += 1
    else:
        vol[a[i]] = True
L = 1
R = N+1

while True:
    while vol[L]: L += 1
    while (R != 0 and vol[R] == False): R -= 1
    if sold >= 2:
        sold -= 2
        vol[L] = True
    else:
        if L>=R: break
        vol[R] = False
        sold += 1

print(L-1)
