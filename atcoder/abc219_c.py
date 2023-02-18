# https://atcoder.jp/contests/abc219/tasks/abc219_c
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

X = input()
N = int(input())
S = [input() for _ in range(N)]
dX = dict(zip(X, range(26)))
# print(dX)
T = []
for i in range(N):
    tmp = ''
    for c in S[i]:
        tmp += chr(dX[c]+ord('a'))
    T.append(tmp)
# print(T)
T.sort()
for i in range(N):
    ans = ''
    for c in T[i]:
        ans += X[ord(c)-ord('a')]
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
