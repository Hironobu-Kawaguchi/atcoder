# https://atcoder.jp/contests/abc223/tasks/abc223_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

S = input().rstrip()
n = len(S)
mn = S
mx = S

for i in range(n):
    tmp = S[i:] + S[:i]
    # print(i, tmp)
    if tmp<mn: mn = tmp
    if tmp>mx: mx = tmp

print(mn)
print(mx)


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
