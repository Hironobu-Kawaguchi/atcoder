# https://atcoder.jp/contests/abc303/tasks/abc303_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M, H, K = map(int, input().split())
S = input()
items = set()
for i in range(M):
    x, y = map(int, input().split())
    items.add((x, y))
used = set()

life, x, y = H, 0, 0
for s in S:
    if s == 'R':
        x += 1
    elif s == 'L':
        x -= 1
    elif s == 'U':
        y += 1
    elif s == 'D':
        y -= 1
    life -= 1

    if life < 0:
        print('No')
        exit()
    if (x, y) in items and (x, y) not in used and life < K:
        life = K
        used.add((x, y))
print('Yes')
