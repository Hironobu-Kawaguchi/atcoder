# https://atcoder.jp/contests/abc306/tasks/abc306_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(input().split())
idx_list = [[] for _ in range(N)]
for i in range(N*3):
    idx_list[int(A[i])-1].append(i)
# print(idx_list)
f_list = []
for i in range(N):
    f_list.append((idx_list[i][1], i+1))
# print(f_list)
f_list.sort()
ans = []
for i in range(N):
    ans.append(f_list[i][1])
print(*ans)


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
