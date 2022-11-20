# https://atcoder.jp/contests/abc278/tasks/abc278_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def f(tm):
    h, m = divmod(tm, 60)
    h1, h2 = divmod(h, 10)
    m1, m2 = divmod(m, 10)
    if (h1*10+m1<24 and h2*10+m2<60):
        return True, h, m
    return False, h, m

H, M = map(int, input().split())
tm = H*60+M

while True:
    flg, h, m = f(tm)
    if flg:
        if h==24:
            print(0, 0)
        else:
            print(h, m)
        break
    tm += 1




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
