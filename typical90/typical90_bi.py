# https://atcoder.jp/contests/typical90/tasks/typical90_bi
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import deque

Q = int(input())
dq = deque([])
for i in range(Q):
    t, x = map(int, input().split())
    if t==1:
        dq.appendleft(x)
    elif t==2:
        dq.append(x)
    else:
        print(dq[x-1])


# import array

# Q = int(input())
# arr = array.array('i')
# for i in range(Q):
#     t, x = map(int, input().split())
#     if t==1:
#         arr.insert(0, x)
#     elif t==2:
#         arr.append(x)
#     else:
#         print(arr[x-1])


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
