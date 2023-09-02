# https://atcoder.jp/contests/abc264/tasks/abc264_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

H = [[0] * 15 for _ in range(15)]
for i in range(1, 9, 2):
    for r in range(15):
        for c in range(15):
            if abs(r-7)==i and abs(c-7)<=i:
                H[r][c] = 1
            if abs(c-7)==i and abs(r-7)<=i:
                H[r][c] = 1

for r in range(15):
    print(H[r], file=sys.stderr)

R, C = map(int, input().split())
if H[R-1][C-1]:
    print('black')
else:
    print('white')


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
