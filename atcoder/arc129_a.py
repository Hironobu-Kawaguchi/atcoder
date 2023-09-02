# https://atcoder.jp/contests/arc129/tasks/arc129_a
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, L, R = map(int, input().split())
ans = 0
for i in range(60):
    if N >> i & 1:
        l = max(L, 1 << i)
        r = min(R, (1 << (i+1)) - 1)
        if l <= r:
            ans += r - l + 1
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
