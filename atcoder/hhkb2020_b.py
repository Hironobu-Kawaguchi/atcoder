# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_b
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

H, W = map(int, input().split())
S = ['' for _ in range(H)]
for i in range(H):
    S[i] = input()
ans = 0
for i in range(H-1):
    for j in range(W):
        if S[i][j] == '.' and S[i+1][j] == '.':
            ans += 1
for i in range(H):
    for j in range(W-1):
        if S[i][j] == '.' and S[i][j+1] == '.':
            ans += 1
print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
