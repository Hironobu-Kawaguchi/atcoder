# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_b
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

A, B, C = map(int, input().split())
K = int(input())

ans = 0
while B <= A:
    ans += 1
    B *= 2
while C <= B:
    ans += 1
    C *= 2
if ans <= K:
    print("Yes")
else:
    print("No")



# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
