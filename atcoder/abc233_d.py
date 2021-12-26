# https://atcoder.jp/contests/abc233/tasks/abc233_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import bisect

N, K = map(int, input().split())
A = list(map(int, (input().split())))

cumA = [0]
for a in A:
    cumA.append(cumA[-1]+a)

d = dict()
for i in range(N+1):
    if cumA[i] not in d:
        d[cumA[i]] = [i]
    else:
        d[cumA[i]].append(i)

ans = 0
for j in range(1, N+1):
    now = cumA[j] - K
    if now not in d: continue
    ans += bisect.bisect_left(d[now], j)

print(ans)


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
