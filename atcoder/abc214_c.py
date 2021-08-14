# https://atcoder.jp/contests/ABC214/tasks/abc214_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

INF = 1001001001
N = int(input())
S = list(map(int, (input().split())))
S = S+S
# print(S)
cumS = [0]
for s in S:
    cumS.append(cumS[-1]+s)
# print(cumS)
T = list(map(int, (input().split())))
Tidx = [(t, i) for i, t in enumerate(T)]
Tidx.sort()
# print(T)
ans = [INF]*N
for t, i in Tidx:
    if ans[i]<=t: continue
    ans[i] = t
    for j in range(N-1):
        if ans[(i+j+1)%N] < ans[(i+j)%N] + S[(i+j)%N]: break
        ans[(i+j+1)%N] = ans[(i+j)%N] + S[(i+j)%N]

for i in range(N):
    print(ans[i])


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
