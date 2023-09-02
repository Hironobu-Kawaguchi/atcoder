# https://atcoder.jp/contests/arc161/tasks/arc161_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
A.sort()
S = [0] * N
for i in range(N//2+1):
    S[i*2] = A[i]
for i in range(N//2+1, N):
    S[(i-N//2)*2-1] = A[i]
# print(S)
ans = 'Yes'
for i in range(N-1):
    if S[i] == S[i+1]:
        ans = 'No'
        break
print(ans)

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
