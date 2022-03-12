# https://atcoder.jp/contests/abc241/tasks/abc241_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import Counter

def main():
    N, M = map(int, input().split())
    A = list(map(int, (input().split())))
    cntA = Counter(A)
    B = list(map(int, (input().split())))
    cntB = Counter(B)
    for k, v in cntB.items():
        if k in cntA and cntA[k]>=v: continue
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
