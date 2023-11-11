# https://atcoder.jp/contests/abc244/tasks/abc244_b
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
muki = 0

x, y = 0, 0
for i in range(N):
    if S[i]=='S':
        x += dx[muki]
        y += dy[muki]
    elif S[i]=='R':
        muki = (muki+1)%4
print(x, y)
