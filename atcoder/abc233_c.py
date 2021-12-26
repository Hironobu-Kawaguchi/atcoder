# https://atcoder.jp/contests/abc233/tasks/abc233_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, X = map(int, input().split())
L = [[int(i) for i in input().split()] for _ in range(N)]
ans = 0

def dfs(v, i):
    global ans
    if i==N:
        if v==X: ans += 1
        return
    for j in range(1, len(L[i])):
        dfs(v*L[i][j], i+1)
    return

dfs(1, 0)
print(ans)


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
