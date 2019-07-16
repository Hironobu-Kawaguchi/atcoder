# https://atcoder.jp/contests/abc041/tasks/abc041_c

import numpy as np

N = int(input())
a = np.array(list(map(int, input().split())))
ans = np.argsort(a)[::-1] + 1

for i in ans:
    print(i)
