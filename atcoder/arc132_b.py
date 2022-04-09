# https://atcoder.jp/contests/arc132/tasks/arc132_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

n = int(input())
p = list(map(int, (input().split())))

flg = False
for i in range(n):
    if p[i]==1:
        pos = i
        if p[(i+1)%n]==2: flg = True
if flg:
    ans = min(pos, n-pos+2)
else:
    ans = min(pos+2, n-pos)

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
