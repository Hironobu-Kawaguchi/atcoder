# https://atcoder.jp/contests/ABC204/tasks/abc204_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import bisect

N = int(input())
T = list(map(int, (input().split())))
s = set([0])
sum_T = 0
for i in range(N):
    sum_T += T[i]
    for j in list(s):
        s.add(j+T[i])
lst = sorted(list(s))
idx = bisect.bisect_left(lst, (sum_T+1)//2)
ans = lst[idx]
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