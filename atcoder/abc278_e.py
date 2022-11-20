# https://atcoder.jp/contests/abc278/tasks/abc278_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# from collections import defaultdict
import copy

H, W, N, h, w = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
# print(A)
# d = defaultdict(int)
cnt = [0] * (N+1)
for i in range(H):
    for j in range(W):
        # if (i<h and j<w): continue
        # d[A[i][j]] += 1
        cnt[A[i][j]] += 1
ans = [[0]*(W-w+1) for _ in range(H-h+1)]
for k in range(H-h+1):
    cnt_kl = copy.copy(cnt)
    for l in range(W-w+1):
        if l==0:
            for i in range(k, k+h):
                for j in range(l, l+w):
                    cnt_kl[A[i][j]] -= 1
        else:
            for i in range(k, k+h):
                cnt_kl[A[i][l-1]] += 1
                cnt_kl[A[i][l+w-1]] -= 1
        tmp = 0
        for ii in range(1, N+1):
            if cnt_kl[ii]>0:
                tmp += 1
        ans[k][l] = tmp

for k in range(H-h+1):
    print(*ans[k])




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
