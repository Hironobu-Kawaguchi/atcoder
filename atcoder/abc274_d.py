# https://atcoder.jp/contests/abc274/tasks/abc274_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, x, y = map(int, input().split())
A = list(map(int, (input().split())))

x_set = set([A[0]])
y_set = set([0])

for i in range(1, N):
    if i%2:
        y_list = list(y_set)
        y_set = set()
        for j in y_list:
            y_set.add(j+A[i])
            y_set.add(j-A[i])
    else:
        x_list = list(x_set)
        x_set = set()
        for j in x_list:
            x_set.add(j+A[i])
            x_set.add(j-A[i])
# print(x_set, y_set)
if x in x_set and y in y_set:
    print('Yes')
else:
    print('No')



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
