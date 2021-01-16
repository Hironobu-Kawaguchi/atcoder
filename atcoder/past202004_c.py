# https://atcoder.jp/contests/past202004-open/tasks/past202004_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
S = []
for i in range(N):
    s = input()
    # print(s)
    S.append(list(s))
# print(S)
for i in range(N-2, -1, -1):
    for j in range(N-1-i, N+i):
        flg = False        
        if S[i+1][j-1]=='X': flg = True
        if S[i+1][j]=='X':   flg = True
        if S[i+1][j+1]=='X': flg = True
        if flg:
            S[i][j] = 'X'
for i in range(N):
    print(''.join(S[i]))

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
