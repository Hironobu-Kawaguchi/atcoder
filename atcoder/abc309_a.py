# https://atcoder.jp/contests/abc309/tasks/abc309_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())

def main(A, B):
    A -= 1; B -= 1
    ax, ay = divmod(A, 3)
    # print(ax, ay, file=sys.stderr)
    bx, by = divmod(B, 3)
    # print(bx, by, file=sys.stderr)
    # if (ax==bx and abs(ay-by)==1) or (ay==by and abs(ax-bx)==1):
    if (ax==bx and abs(ay-by)==1):
        print('Yes')
        print(A, B, ax, ay, bx, by, 'Yes', file=sys.stderr)
    else:
        print('No')
        print(A, B, ax, ay, bx, by, 'No', file=sys.stderr)

main(A, B)

# for a in range(1,9):
#     for b in range(a+1, 10):
#         main(a, b)

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
