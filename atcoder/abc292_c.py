# https://atcoder.jp/contests/abc292/tasks/abc292_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
cnt = [0]*N
for i in range(1, N):
    for j in range(i, N, i):
        cnt[j] += 1
# print(cnt)

ans = 0
for i in range(1, N):
    ans += cnt[i] * cnt[N-i]
print(ans)



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
