# https://atcoder.jp/contests/abc208/tasks/abc208_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

P = int(input())
f = [0]*11
f[0] = 1
for i in range(1,11):
    f[i] = f[i-1] * i
ans = 0
for i in range(10,0,-1):
    if P>=f[i]:
        d = P // f[i]
        ans += d
        P -= d * f[i]
    if P==0:
        break
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
