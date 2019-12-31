# https://atcoder.jp/contests/arc017/tasks/arc017_2

import numpy as np
import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
A = np.array([readline() for _ in range(N)], dtype=np.int32)
# print(A)
B = np.zeros(N,dtype=np.bool)
B[1:] = (A[1:] > A[:-1])
# print(B)

start = np.arange(N)
start[B] = 0
# print(start)

np.maximum.accumulate(start, out = start)
# print(start)

L = np.arange(1, N+1) - start
# print(L)
ans = (L >= K).sum()
# print(L >= K)
print(ans)
