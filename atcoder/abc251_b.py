# https://atcoder.jp/contests/abc251/tasks/abc251_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, W = map(int, input().split())
A = list(map(int, (input().split())))

flg = [0]*(W+1)
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i==j==k and A[i]<=W:     flg[A[i]] = 1
            elif i==j and A[i]+A[k]<=W: flg[A[i]+A[k]] = 1
            elif i==k and A[i]+A[j]<=W: flg[A[i]+A[j]] = 1
            elif j==k and A[i]+A[j]<=W: flg[A[i]+A[j]] = 1
            elif A[i]+A[j]+A[k]<=W:     flg[A[i]+A[j]+A[k]] = 1
ans = 0
for i in range(W+1):
    if flg[i]: 
        ans += 1
        # print(i)
print(ans)


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
