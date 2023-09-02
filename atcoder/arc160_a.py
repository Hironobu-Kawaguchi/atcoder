# https://atcoder.jp/contests/arc160/tasks/arc160_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, (input().split())))

a = 1           # 最小の順位
b = N*(N+1)//2  # 最大の順位
for l in range(N):      # 前から順に探索していく
    small, large = [], []
    for r in range(l+1, N):     # まだ確定していない部分列の中で，A[l]より小さいものと大きいものを分ける
        if A[r] < A[l]:
            small.append(A[r])
        elif A[r] > A[l]:
            large.append(A[r])
    x = -1
    if K-a < len(small):    # K番目の順位がsmallに含まれる
        small.sort()
        x = small[K-a]
    if b-K < len(large):    # K番目の順位がlargeに含まれる
        large.sort(reverse=True)
        x = large[b-K]
    if x!=-1:   # K番目の順位がsmallかlargeに含まれるので，lを固定してf(l, r)を実行
        r = l
        while A[r]!=x:      # K番目の順位を持つidxをrとする
            r += 1
        A = A[:l] + A[l:r+1][::-1] + A[r+1:]    # f(l, r)を実行
        break
    a += len(small)
    b -= len(large)
print(*A)



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
