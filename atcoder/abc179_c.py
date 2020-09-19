# https://atcoder.jp/contests/abc179/tasks/abc179_c

import numpy as np
n = int(input())
ans = np.zeros(n, dtype=np.int64)
for a in range(1,n):
    ans[a::a] += 1
print(ans.sum())

# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
