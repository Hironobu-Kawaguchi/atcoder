# https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

D = int(input())
c = list(map(int, (input().split())))
s = [[int(i) for i in input().split()] for _ in range(D)]
t = [int(input()) for _ in range(D)]

def  compute_score(D, c, s, t):
    v = [0] * D
    last = [-1] * 26
    for d in range(D):
        if d: v[d] = v[d-1]
        v[d] += s[d][t[d]-1]
        last[t[d]-1] = d
        for j in range(26):
            v[d] -= c[j] * (d - last[j])
    return v

score = compute_score(D, c, s, t)
for v in score:
    print(v)


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
