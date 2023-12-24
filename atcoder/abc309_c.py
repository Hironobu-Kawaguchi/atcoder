# https://atcoder.jp/contests/abc309/tasks/abc309_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
ab = []
sm = 0
for i in range(N):
    a, b = map(int, input().split())
    ab.append([a, b])
    sm += b
ab.sort()
# print(ab, file=sys.stderr)
if sm<=K:
    print(1)
    exit()
for i in range(N):
    sm -= ab[i][1]
    if sm<=K:
        print(ab[i][0]+1)
        exit()


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
