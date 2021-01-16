# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

n = int(input())
a = list(map(int, (input().split())))
b = list(map(int, (input().split())))
max_a = [0]
ans = [0]
for i in range(n):
    max_a.append(max(max_a[-1], a[i]))
    ans.append(max(ans[-1], b[i]*max_a[-1]))
for i in range(1,n+1):
    print(ans[i])


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
