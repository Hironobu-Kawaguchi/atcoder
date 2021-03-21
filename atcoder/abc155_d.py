# https://atcoder.jp/contests/abc155/tasks/abc155_d

import numpy as np
import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = np.array(input().split(), np.int64)

A = np.sort(A)
zero = A[A == 0]
pos = A[A > 0]
neg = A[A < 0]


def f(x):
    """count the number of products , <= x"""
    cnt_tpl = 0
    # zero and ...
    if x >= 0:
        cnt_tpl += len(zero) * N
    # positive and ...
    cnt_tpl += np.searchsorted(A, x // pos, side='right').sum()
    # negative and ...
    cnt_tpl += (N - np.searchsorted(A, (-x - 1) // (-neg), side='right')).sum()
    # a^2
    cnt_tpl -= np.count_nonzero(A * A <= x)
    assert cnt_tpl % 2 == 0
    return cnt_tpl // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    x = (left + right) // 2
    if f(x) >= K:
        right = x
    else:
        left = x


print(right)



# TLE
# import sys
# input = sys.stdin.buffer.readline
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()

# def ok(x):
#     res = 0
#     for i in range(N):
#         if A[i]<0:
#             left, right = -1, N
#             while left + 1 < right:
#                 c = (left + right) // 2
#                 if A[c]*A[i] < x: right = c
#                 else:             left  = c
#             res += N - right
#         else:
#             left, right = -1, N
#             while left + 1 < right:
#                 c = (left + right) // 2
#                 if A[c]*A[i] < x: left  = c
#                 else:             right = c
#             res += right
#         if A[i]*A[i] < x:
#             res -= 1
#     res //= 2
#     return res < K

# INF = 10**18+1
# l, r = -INF, INF
# while l+1<r:
#     x = (l+r)//2
#     if ok(x):
#         l = x
#     else:
#         r = x
# print(l)
