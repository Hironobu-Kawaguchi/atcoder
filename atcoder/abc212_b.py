# https://atcoder.jp/contests/ABC212/tasks/abc212_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

X = list(map(int, list(input().rstrip())))
# print(X)
flag1 = True
flag2 = True
for i in range(3):
    if X[i+1]!=X[i]:
        flag1 = False
        # print("flag1", i, X[i+1], X[i])
    if X[(i+1)%4] != (X[i]+1)%10:
        flag2 = False
        # print("flag2", i, X[(i+1)%4], X[i])
if flag1 or flag2:
    print("Weak")
else:
    print("Strong")


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
