# https://atcoder.jp/contests/abc305/tasks/abc305_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import bisect

N = int(input())
A = list(map(int, (input().split())))
Q = int(input())

Acum = []
for i in range(N):
    if i==0:
        Acum.append(0)
    elif i%2==1:
        Acum.append(Acum[-1])
    else:
        Acum.append(Acum[-1] + (A[i]-A[i-1]))
# print(Acum)

for qi in range(Q):
    l, r = map(int, input().split())
    lidx = bisect.bisect_left(A, l)
    ridx = bisect.bisect_right(A, r) - 1
    # print(lidx, ridx)
    if ridx==-1:
        print(0)
        continue
    ans = Acum[ridx] - Acum[lidx]
    if lidx%2==0:
        ans += A[lidx]-l
    if ridx%2:
        ans += r-A[ridx]
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
