# https://atcoder.jp/contests/abc308/tasks/abc308_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque

chr = "snuke"

H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)
if S[0][0]!='s':
    print("No")
    exit()
vi = [0, 1, 0, -1]
vj = [1, 0, -1, 0]
q = deque([(0, 0, 0)])
gone = [[False] * W for _ in range(H)]
gone[0][0] = True

while q:
    # print(q)
    i, j, d = q.popleft()
    if i==H-1 and j==W-1:
        print("Yes")
        exit()
    for v in range(4):
        ni = i + vi[v]
        nj = j + vj[v]
        if ni<0 or ni>=H or nj<0 or nj>=W: continue
        if S[ni][nj] == chr[(d+1)%5] and not gone[ni][nj]:
            q.append((ni, nj, d+1))
            gone[ni][nj] = True
print("No")
