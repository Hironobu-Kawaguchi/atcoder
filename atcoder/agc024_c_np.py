# https://atcoder.jp/contests/agc024/tasks/agc024_c

import sys
input = sys.stdin.buffer.readline
import numpy as np
N = int(input())
A = np.array([int(input()) for _ in range(N)] + [0], dtype=np.int64)
# print(A)
ans = (A[:-1][A[:-1] >= A[1:]]).sum()
if any(A[:-1] + 1 < A[1:]):
    ans = -1
elif A[0] != 0:
    ans = -1

print(ans)
