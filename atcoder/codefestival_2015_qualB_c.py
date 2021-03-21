# https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_c
import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

def main():
    N, M = map(int, input().split())
    A = list(map(int, (input().split())))
    A.sort(reverse=True)
    B = list(map(int, (input().split())))
    B.sort(reverse=True)
    if N<M:
        return 'NO'
    for i in range(M):
        if A[i]<B[i]:
            return 'NO'
    return 'YES'

print(main())


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
