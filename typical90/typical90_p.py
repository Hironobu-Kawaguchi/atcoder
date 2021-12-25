# https://atcoder.jp/contests/typical90/tasks/typical90_p
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A, B, C = map(int, input().split())
ans = 10000
for a in range(10000):
    if A*a>N: continue
    for b in range(10000-a):
        if A*a+B*b>N: continue
        if (N-A*a-B*b)%C==0:
            ans = min(ans, a+b+(N-A*a-B*b)//C)
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
