# https://atcoder.jp/contests/abc308/tasks/abc308_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

S = list(map(int, (input().split())))
ans = "Yes"
for i in range(7):
    if S[i]>S[i+1]:
        ans = "No"
        break
for i in range(8):
    if S[i]<100 or S[i]>675:
        ans = "No"
        break
    if S[i]%25!=0:
        ans = "No"
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
