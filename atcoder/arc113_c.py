# https://atcoder.jp/contests/arc113/tasks/arc113_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

from string import ascii_lowercase
S = input()
N = len(S)
d = dict(zip(ascii_lowercase, range(26)))
# print(d)
right_list = [0]*26
right_list[d[S[N-1]]] += 1
right_list[d[S[N-2]]] += 1

ans = 0
for i in range(N-3, -1, -1):
    if S[i]==S[i+1]:
        ans += (N-i-1) - right_list[d[S[i]]]
        right_list = [0]*26
        right_list[d[S[i]]] += N-i
    else:
        right_list[d[S[i]]] += 1
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
