# https://atcoder.jp/contests/abc102/tasks/abc102_b

import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

ans = A.max() - A.min()
print(ans)
