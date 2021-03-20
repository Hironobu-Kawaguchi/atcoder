# https://atcoder.jp/contests/abc195/tasks/abc195_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

INF = 1001001001
A, B, W = map(int, input().split())
W *= 1000
minN, maxN = INF, -INF
for i in range(W//B, W//A + 1):
    if A*i <= W <= B*i:
        minN = min(minN, i)
        maxN = max(maxN, i)
if minN>maxN:
    print('UNSATISFIABLE')
else:
    print(minN, maxN)


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
