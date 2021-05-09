# https://atcoder.jp/contests/arc118/tasks/arc118_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# import math
k, n, m = map(int, input().split())
a = list(map(int, (input().split())))
b = []
sumb = 0
for x in a:
    y = x*m//n
    b.append(y)
    sumb += y
# print(b)
rest = m -sumb
c = []
for i in range(k):
    z = a[i]*m - b[i]*n
    c.append((z,i))
c.sort(reverse=True)
# print(c)
for i in range(rest):
    b[c[i][1]] += 1
print(*b)


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
