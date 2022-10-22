# https://atcoder.jp/contests/abc274/tasks/abc274_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))

# pos = [-1]*(2*N+2)
# pos[1] = 1
ans = [-1]*(2*N+2)
ans[1] = 0
for i in range(N):
    # pos[2*(i+1)] = 2*pos[A[i]]
    ans[2*(i+1)] = ans[A[i]] + 1
    # pos[2*(i+1)+1] = 2*pos[A[i]] + 1
    ans[2*(i+1)+1] = ans[A[i]] + 1
# print(pos)

for i in range(1, 2*N+2):
    print(ans[i])


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
