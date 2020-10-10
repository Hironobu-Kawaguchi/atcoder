# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c
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

N = int(input())
p = list(map(int, (input().split())))
num = [False] * 200001

now = 0
ans = []
for i in range(N):
    num[p[i]] = True
    while num[now] == True:
        now += 1
    ans.append(now)
for i in range(N):
    print(ans[i])

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
