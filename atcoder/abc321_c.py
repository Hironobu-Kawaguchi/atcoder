# https://atcoder.jp/contests/abc321/tasks/abc321_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

K = int(input())
lst = []

for bi in range(1, 1<<10):
    s = ""
    for i in range(10):
        if bi>>i&1:
            s += str(i)
    n = int(s[::-1])
    if n > 0:
        lst.append(n)
lst.sort()
# print(len(lst), lst)
print(lst[K-1])
