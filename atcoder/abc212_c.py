# https://atcoder.jp/contests/ABC212/tasks/abc212_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
A = list(map(int, (input().split())))
A.sort()
B = list(map(int, (input().split())))
B.sort()

i, j = 0, 0
ans = 1001001001
while True:
    ans = min(ans, abs(A[i]-B[j]))
    if ans==0: break
    if i==N-1 and j==M-1: break
    if   i==N-1: j += 1
    elif j==M-1: i += 1
    elif A[i]<B[j]: i += 1
    elif A[i]>B[j]: j += 1
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
