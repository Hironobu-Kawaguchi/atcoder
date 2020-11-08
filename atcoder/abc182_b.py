# https://atcoder.jp/contests/abc182/tasks/abc182_b
# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()

N = int(input())
A = list(map(int, (input().split())))
max_gcd = 0
ans = 2
for k in range(2,1001):
    cnt = 0
    for a in A:
        if a%k==0: cnt += 1
    if cnt > max_gcd:
        ans = k
        max_gcd = cnt
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
