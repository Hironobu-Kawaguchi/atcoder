# https://atcoder.jp/contests/ABC282/tasks/abc282_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
S = [input() for _ in range(N)]
# print(S)
ans = 0
for x in range(N):
    for y in range(x+1, N):
        flg = True
        for j in range(M):
            if S[x][j]=='x' and S[y][j]=='x': flg = False
        if flg: ans += 1
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
