# https://atcoder.jp/contests/arc133/tasks/arc133_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))

def f(x):
    a = []
    for i in range(N):
        if A[i]!=x:
            a.append(A[i])
    return a

x = A[-1]
for i in range(N-1):
    if A[i]>A[i+1]:
        x = A[i]
        break

a = f(x)
print(*a)

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
