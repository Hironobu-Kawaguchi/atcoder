# https://atcoder.jp/contests/arc023/tasks/arc023_2

import numpy as np
import sys
readline = sys.stdin.buffer.readline

R, C, D = map(int, readline().split())
A = np.array([readline().split() for _ in range(R)], dtype=np.int32)
# print(A)

dist = np.arange(R)[:, None] + np.arange(C)[None, :]
select = (dist%2 == D%2) & (dist <= D)
ans = (A * select).max()
print(ans)
