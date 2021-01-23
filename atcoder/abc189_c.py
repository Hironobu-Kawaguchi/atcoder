# https://atcoder.jp/contests/abc189/tasks/abc189_c
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def getRectangleArea(a):
    N = len(a)
    rectangle = [0] * N
    stk = []
    for i in range(N):
        while len(stk) > 0:
            righttail = stk[-1]
            if a[righttail] > a[i]:
                rectangle[righttail] = i
                stk.pop()
                continue
            break
        stk.append(i)

    for i in stk:
        rectangle[i] = N
    return rectangle

N = int(input())
A = list(map(int, (input().split())))
rc = getRectangleArea(A)
# print(rc)
rc2 = getRectangleArea(A[::-1])
rc2.reverse()
# print(rc2)
ans = 0
for i in range(N):
    ans = max(ans, A[i]*(rc[i]-(N-rc2[i])))

for i in range(N):
    ans = max(ans, A[i]*(rc[i]-i))

print(ans)

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
