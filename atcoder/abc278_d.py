# https://atcoder.jp/contests/abc278/tasks/abc278_d
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
Q = int(input())

st = set(range(N))
# print(st)
default = -1

def f(i):
    if i in st:
        return A[i]
    else:
        return default

for qi in range(Q):
    query = input()
    if query[0]=='1':
        t, x = map(int, query.split())
        default = x
        st = set()
    elif query[0]=='2':
        t, i, x = map(int, query.split())
        A[i-1] = f(i-1) + x
        st.add(i-1)
    else:
        # print(query)
        t, i = map(int, query.split())
        print(f(i-1))



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
