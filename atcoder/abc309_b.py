# https://atcoder.jp/contests/abc309/tasks/abc309_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = [list(input()) for _ in range(N)]
ans = [[-1] * N for _ in range(N)]
# print(A, file=sys.stderr)

for i in range(1, N-1):
    for j in range(1, N-1):
        ans[i][j] = A[i][j]
for i in range(N-1):
    ans[0][i+1] = A[0][i]
    ans[N-1][i] = A[N-1][i+1]
    ans[i][0] = A[i+1][0]
    ans[i+1][N-1] = A[i][N-1]
for i in range(N):
    print(*ans[i], sep='')



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
