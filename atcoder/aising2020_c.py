# https://atcoder.jp/contests/aising2020/tasks/aising2020_c

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)


# def main():
#     # @lru_cache(None)
#     # def dfs():
#     #     return
#     A, B = map(int, input().split())
#     print(A*B)
#     return

# main()

from itertools import product
N = int(input())
M = int(N**0.5)
ans = [0] * N
for x, y, z in product(range(1, M+1), repeat=3):
    i = x*x + y*y + z*z + x*y + y*z + z*x
    if i <= N:
        ans[i-1] += 1
for i in range(N):
    print(ans[i])

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
