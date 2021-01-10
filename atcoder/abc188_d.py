# https://atcoder.jp/contests/abc188/tasks/abc188_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

N, C = map(int, input().split())
d = defaultdict(int)
for i in range(N):
    a, b, c = map(int, input().split())
    d[a] += c
    d[b+1]   -= c
k_pre = 0
now = 0
ans = 0
for k, v in sorted(d.items()):
    ans += (k-k_pre) * min(now, C)
    # print(ans)
    now += v
    k_pre = k

print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
