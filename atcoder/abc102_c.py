# https://atcoder.jp/contests/abc102/tasks/abc102_c

import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

b = np.median((A - np.arange(1, N+1)))
ans = np.abs(A - b - np.arange(1, N+1)).sum()

print(int(ans))
