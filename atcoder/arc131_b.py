# https://atcoder.jp/contests/arc131/tasks/arc131_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

def next_color(i, j):
    ret = set()
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < H and 0 <= nj < W:
            if c[ni][nj] != '.':
                ret.add(int(c[ni][nj]))
    return ret

def new_color(color_set):
    for c in range(1, 6):
        if c not in color_set:
            return c

for i in range(H):
    for j in range(W):
        if c[i][j] != '.':
            c[i][j] = c[i][j]
        else:
            c[i][j] = str(new_color(next_color(i, j)))
for i in range(H):
    print(''.join(c[i]))


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
