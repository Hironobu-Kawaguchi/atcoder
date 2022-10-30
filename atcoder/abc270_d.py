# https://atcoder.jp/contests/abc270/tasks/abc270_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, (input().split())))

dp = [0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    for j in range(K):
        if A[j]>i: continue
        dp[i] = max(dp[i], i - dp[i - A[j]])
# print(dp)
print(dp[N])


# WA
# import bisect

# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A.sort()

# lst = []
# while N>0:
#     idx = bisect.bisect_right(A, N)
#     # print(N, idx, lst)
#     N -= A[idx-1]
#     lst.append(A[idx-1])
# ans = 0
# for i, x in enumerate(lst):
#     if i%2==0:
#         ans += x
# print(ans)


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
