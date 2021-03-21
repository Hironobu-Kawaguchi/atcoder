# https://atcoder.jp/contests/abc185/tasks/abc185_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

N, M, T = map(int, input().split())
lst = []
now = 0
for i in range(M):
    A, B = map(int, input().split())
    lst.append(now-A)
    lst.append(B-A)
    now = B
lst.append(now-T)
# print(lst)

ans = 'Yes'
now = N
for c in lst:
    now += c
    if now<=0:
        ans = 'No'
    if now>N:
        now = N
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
