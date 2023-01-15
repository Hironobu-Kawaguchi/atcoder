# https://atcoder.jp/contests/arc153/tasks/arc153_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
N -= 1
lst = [0] * 6
for i in range(6):
    N, tmp = divmod(N, 10)
    lst[i] = tmp
lst.reverse()
# print(lst)
ans = (lst[0]+1)*110000000 + lst[1]*1000000 + lst[2]*100000 + lst[3]*11000 + lst[4]*101 + lst[5]*10
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
