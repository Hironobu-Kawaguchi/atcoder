# https://atcoder.jp/contests/ABC285/tasks/abc285_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = input()
# print(S)
ans = 0
keta = 1
for i in range(len(S)-1, -1, -1):
    ans += keta * (ord(S[i]) - ord('A') + 1)
    keta *= 26
    # print(i, ans, keta)
print(ans)
