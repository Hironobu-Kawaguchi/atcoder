# https://atcoder.jp/contests/abc293/tasks/abc293_a
# from numba import njit
# from functools import lru_cache


# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = input()
T = ''
for i in range(0, len(S), 2):
    T += S[i+1]
    T += S[i]
print(T)


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
