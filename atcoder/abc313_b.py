# https://atcoder.jp/contests/abc313/tasks/abc313_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())

win_lose = [[0]*2 for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    win_lose[A][0] += 1
    win_lose[B][1] += 1

ok = True
cand = []
for i in range(N):
    if win_lose[i][0]==0 and win_lose[i][1]==0:
        ok = False
    if win_lose[i][0]>0 and win_lose[i][1]==0:
        cand.append(i)

if not ok or len(cand)>=2:
    print(-1)
else:
    print(cand[0]+1)
