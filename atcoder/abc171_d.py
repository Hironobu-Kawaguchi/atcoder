# https://atcoder.jp/contests/abc171/tasks/abc171_c

# import sys
# def input(): return sys.stdin.readline().rstrip()
# input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# from numba import njit
# from functools import lru_cache
# sys.setrecursionlimit(10 ** 7)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# @njit(cache=True)


# def main():
#     # @lru_cache(None)
#     # def dfs():
#     #     return
#     A, B = map(int, input().split())
#     print(A*B)
#     return

# main()

# from string import ascii_lowercase
from collections import Counter
N = int(input())
A = list(map(int, (input().split())))
Q = int(input())
Cnt = Counter(A)
ans = sum(A)
for i in range(Q):
    b, c = map(int, input().split())
    if b in Cnt:
        ans += Cnt[b] * (c-b)
        Cnt[c] += Cnt[b]
        Cnt[b] = 0
    print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
