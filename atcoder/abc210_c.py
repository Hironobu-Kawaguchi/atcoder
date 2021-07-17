# https://atcoder.jp/contests/ABC210/tasks/abc210_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
c = list(map(int, (input().split())))
d = dict()

for i in range(K):
    if c[i] in d:
        d[c[i]] += 1
    else:
        d[c[i]] = 1
# print(d)

ans = len(d)
for i in range(N-K):
    if d[c[i]]==1:
        d.pop(c[i])
    else:
        d[c[i]] -= 1
    if c[i+K] in d:
        d[c[i+K]] += 1
    else:
        d[c[i+K]] = 1
    ans = max(ans, len(d))
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
