# https://atcoder.jp/contests/abc170/tasks/abc170_b

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)


def main():
#     # @lru_cache(None)
#     # def dfs():
#     #     return
#     A, B = map(int, input().split())
#     print(A*B)
    X, Y = map(int, input().split())
    if Y%2:
        return 'No'
    Y //= 2
    if X <= Y <= 2*X:
        return 'Yes'
    else:
        return 'No'

print(main())


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
