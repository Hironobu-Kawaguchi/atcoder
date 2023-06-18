# https://atcoder.jp/contests/abc292/tasks/abc292_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
cnt = [0]*N
for qi in range(Q):
    c, x = map(int, input().split())
    if c==1:
        cnt[x-1] += 1
    elif c==2:
        cnt[x-1] += 2
    else:
        if cnt[x-1]>=2:
            print("Yes")
        else:
            print("No")


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
