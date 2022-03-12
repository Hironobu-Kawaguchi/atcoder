# https://atcoder.jp/contests/abc243/tasks/abc243_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, X = map(int, input().split())
S = input()

X = list(bin(X))
for c in S:
    if c=='U':
        # X = X[:-1]
        X.pop()
    elif c=='L':
        # X = X + '0'
        X.append('0')
    else:
        # X = X + '1'
        X.append('1')
print(int(''.join(X), 2))

# N, X = map(int, input().split())
# S = input()

# for c in S:
#     if c=='U':
#         X >>= 1
#     elif c=='L':
#         X <<= 1
#     else:
#         X <<= 1
#         X += 1
# print(X)

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
