# https://atcoder.jp/contests/arc134/tasks/arc134_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, L, W = map(int, input().split())
a = list(map(int, (input().split())))

ans = 0
now = 0
for i in range(N-1):
    if a[i]+W<a[i+1]:
        ans += (a[i+1] - (a[i]+W) + W-1)//W
ans += (a[0] + W-1)//W
ans += (L - (a[-1]+W) + W-1)//W
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
