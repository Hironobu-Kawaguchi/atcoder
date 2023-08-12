# https://atcoder.jp/contests/abc310/tasks/abc310_b
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
fs = [[int(i) for i in input().split()] for _ in range(N)]
# print(fs, file=sys.stderr)
fset = []
for i in range(N):
    fset.append(set(fs[i][2:]))
# print(fset, file=sys.stderr)
ans = "No"
for i in range(N):
    for j in range(N):
        if fs[i][0]<fs[j][0]: continue
        if len(fset[i] - fset[j])>0: continue
        if fs[i][0]>fs[j][0] or len(fset[j] - fset[i])>0:
            ans = "Yes"
            # print(i, j, file=sys.stderr)
            break
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
