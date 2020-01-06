# https://atcoder.jp/contests/abc141/tasks/abc141_f

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

N = int(input())
A = np.array([int(x) for x in input().split()],dtype=np.int64)

"""
F_2 上の線形代数。基本変形で簡単な基底を得る。
"""

xor = np.bitwise_xor.reduce(A)

A = np.concatenate([np.array([1<<i for i in range(60) if xor&(1<<i)],np.int64),A])

for k in range(60,-1,-1):
    bit = 1<<k
    one = (A&bit != 0)
    i = np.where(one & (A < (1<<(k+1))))[0]
    if len(i) == 0:
        continue
    i = i[0]
    x = A[i]
    A[one] ^= x
    A[i] = x

A = A[A != 0]
A.sort()
A = A[::-1]

if len(A) > 0:
	red = np.bitwise_xor.reduce(A)
else:
    red = 0
blue = red^xor
answer = red + blue
print(answer)


# from numpy import *
# f=bitwise_xor.reduce
# N=int(input())
# A=array(input().split(),int64)
# X=f(A)
# A=hstack((A,array([1<<i for i in range(60)if X&(1<<i)],int64)))
# for k in range(60)[::-1]:
#   b=1<<k
#   j=A&b!=0
#   i=where(j&(A<2*b))[0]
#   if len(i):i=i[0];x=A[i];A[j]^=x;A[i]=x
# r=f(A)
# print(r+(r^X))


# N = int(input())
# A = list(map(int, input().split()))

# ans = 0

# def dfs(i, red, blue, r, b):
#     if i >= N:
#         return
#     if red == 0:
#         dfs(i+1, A[i], blue, r+1, b)
#         dfs(i+1, red, blue ^ A[i], r, b+1)
#     elif blue == 0:
#         dfs(i+1, red ^ A[i], blue, r+1, b)
#         dfs(i+1, red, A[i], r, b+1)
#     else:
#         dfs(i+1, red ^ A[i], blue, r+1, b)
#         dfs(i+1, red, blue ^ A[i], r, b+1)
#     if i == N-1:
#         global ans
#         ans = max(ans, red + blue)

# dfs(0,0,0,0,0)
# # ans = 6 + 3^5
# print(ans)
