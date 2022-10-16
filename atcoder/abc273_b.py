# https://atcoder.jp/contests/abc273/tasks/abc273_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def f(x, i):
    tmp = 10**i
    left = x // (tmp*10)
    right = x % (tmp*10)
    if right>=5*tmp:
        y = (left+1) * tmp * 10
    else:
        y = left * tmp *10
    return y

X, K = map(int, input().split())
for i in range(K):
    X = f(X, i)
print(X)



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
