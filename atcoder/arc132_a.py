# https://atcoder.jp/contests/arc132/tasks/arc132_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

n = int(input())
R = list(map(int, (input().split())))
C = list(map(int, (input().split())))

ans = ''
q = int(input())
for qi in range(q):
    r, c = map(int, input().split())
    if R[r-1] + C[c-1] <= n:
        ans += '.'
    else:
        ans += '#'
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
