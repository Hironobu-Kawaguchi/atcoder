# https://atcoder.jp/contests/arc138/tasks/arc138_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def main():
    N = int(input())
    A = list(map(int, (input().split())))
    flag = 1
    l, r = 0, N-1
    while l<=r:
        # print(l, r, flag)
        if A[r]^flag:
            r -= 1
        elif A[l]^flag:
            l += 1
            flag = 1 - flag
        else:
            print("No")
            return
    print("Yes")
    return

main()

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
