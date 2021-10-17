# https://atcoder.jp/contests/abc221/tasks/abc221_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
d = dict()

for i in range(N):
    A, B = map(int, input().split())
    if A in d: d[A] += 1
    else:      d[A]  = 1
    if A+B in d: d[A+B] -= 1
    else:      d[A+B]  = -1
# print(d)
ans = [0] * (N+1)
now = 0
pre = 1
for k, v in sorted(d.items()):
    if v==0: continue
    # print(k, v)
    ans[now] += k-pre
    now += v
    pre = k
print(*ans[1:])


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
