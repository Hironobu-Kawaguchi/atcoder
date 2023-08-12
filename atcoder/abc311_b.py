# https://atcoder.jp/contests/abc310/tasks/abc310_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, D = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
now = 0
for i in range(D):
    flg = True
    for j in range(N):
        if S[j][i]=='x':
            ans = max(ans, now)
            now = 0
            flg = False
            break
    if flg:
        now += 1
else:
    if flg:
        ans = max(ans, now)
print(ans)

# for a in range(1,9):
#     for b in range(a+1, 10):
#         main(a, b)

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
