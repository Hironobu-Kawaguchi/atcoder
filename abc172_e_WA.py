# https://atcoder.jp/contests/abc172/tasks/abc172_e

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

MOD = 10**9+7
N, M = map(int, input().split())
f = [M]
p = [M]
for i in range(N-1):
    p.append(p[-1]*(M-i-1)%MOD)
    f.append(((pow(p[-1],2,MOD)-M*(pow(p[-2],2,MOD)-f[-1]))+MOD)%MOD)
print(f[-1])
# print(p)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
