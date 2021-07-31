# https://atcoder.jp/contests/ABC212/tasks/abc212_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

import heapq
Q = int(input())
a = []
heapq.heapify(a)
add_v = 0
for qi in range(Q):
    q = input().rstrip()
    if q[0]=='1':
        _, x = q.split()
        # heapq.heappush(a, int(x))
        heapq.heappush(a, int(x)-add_v)
    elif q[0]=='2':
        _, x = q.split()
        add_v += int(x)
    else:
        x = heapq.heappop(a)
        print(x+add_v)




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
