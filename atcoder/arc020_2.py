# https://atcoder.jp/contests/arc020/tasks/arc020_2

import itertools
import numpy as np
n, c = map(int, input().split())
a = np.array([int(input()) for _ in range(n)])
od = np.bincount(a[1::2], minlength=11)
ev = np.bincount(a[::2], minlength=11)

nochange = max(od[p1] + ev[p2] for p1, p2 in itertools.permutations(range(11), 2))
ans = (n - nochange) * c
print(ans)
