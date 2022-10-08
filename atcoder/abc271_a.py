# https://atcoder.jp/contests/abc271/tasks/abc271_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

dd = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
N = int(input())
ans = ''
div, mod = divmod(N, 16)
ans += dd[div]
ans += dd[mod]
print(ans)
