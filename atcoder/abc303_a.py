# https://atcoder.jp/contests/abc303/tasks/abc303_a
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = input()
T = input()

ok_set = set([('1', 'l'), ('0', 'o')])

for i in range(N):
    if S[i] == T[i]:
        continue
    if tuple(sorted([S[i], T[i]])) in ok_set:
        continue
    print('No')
    sys.exit()
print('Yes')
