# https://atcoder.jp/contests/typical90/tasks/typical90_bw
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
cnt = 1
now = 2
zan = N
while now*now<=zan:
    if zan%now==0:
        zan //= now
        cnt += 1
    else:
        now += 1
# print(cnt)

ans = 0
while cnt>1:
    cnt = (cnt+1)//2
    ans += 1
print(ans)


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
