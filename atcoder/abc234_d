# https://atcoder.jp/contests/ABC234/tasks/abc234_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import heapq

N, K = map(int, input().split())
P = list(map(int, (input().split())))

q = []
heapq.heapify(q)
for i in range(K):
    heapq.heappush(q, P[i])
print(q[0])

for i in range(K, N):
    if q[0]<P[i]:
        heapq.heappushpop(q, P[i])
    print(q[0])



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
