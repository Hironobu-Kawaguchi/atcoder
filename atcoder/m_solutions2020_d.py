# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
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

import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, (input().split())))

lst = []
small, large = 0, 0
for i in range(N):
    if i==0:
        small = A[i]
        large = A[i]
    else:
        if A[i] < large:
            if small < large:
                lst.append((small,large))
            small = A[i]
            large = A[i]
        else:
            large = A[i]
else:
    if small < large:
        lst.append((small,large))
# print(lst)
ans = 1000
for s, l in lst:
    stock, ans = divmod(ans, s)
    ans += stock * l
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
