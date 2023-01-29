# https://atcoder.jp/contests/abc287/tasks/abc287_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# 入力
S = input()
T = input()
N = len(T)
dif = len(S) - N
l = 0
for i in range(N):
    if S[i]==T[i] or S[i]=='?' or T[i]=='?':
        l += 1
    else:
        break
r = 0
for i in range(N-1, -1, -1):
    if S[i+dif]==T[i] or S[i+dif]=='?' or T[i]=='?':
        r += 1
    else:
        break
# print(l, r)

for x in range(N+1):
    if l>=x and r>=N-x:
        print("Yes")
    else:
        print("No")



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
