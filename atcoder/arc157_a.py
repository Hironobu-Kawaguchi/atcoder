# https://atcoder.jp/contests/arc157/tasks/arc157_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

def main():
    N, A, B, C, D = map(int, input().split())
    if B==C==0 and A>0 and D>0:
        print("No")
        return
    if abs(B-C)>=2:
        print("No")
        return
    print("Yes")
    return

main()

# TLE
# def main():
#     N, A, B, C, D = map(int, input().split())
#     cnt_list = [A, B, C, D]
#     dp = [[set() for _ in range(4)] for _ in range(N)]
#     for j in range(4):
#         for j in range(4):
#             dp[0][j].add(tuple(cnt_list))
#     # print(dp)
#     for i in range(N):
#         for j in range(4):
#             if j==0 or j==2:
#                 for k in [0, 1]:
#                     for tp in dp[i][j]:
#                         if tp[k]<1: continue
#                         tp = list(tp)
#                         tp[k] -= 1
#                         dp[i+1][k].add(tuple(tp))
#             else:
#                 for k in [2, 3]:
#                     for tp in dp[i][j]:
#                         if tp[k]<1: continue
#                         tp = list(tp)
#                         tp[k] -= 1
#                         dp[i+1][k].add(tuple(tp))
#     # for i in range(N):
#     #     print(dp[i])
#     ans = "No"
#     for j in range(4):
#         if tuple([0,0,0,0]) in dp[N-1][j]:
#             ans = "Yes"
#     print(ans)

# main()

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
