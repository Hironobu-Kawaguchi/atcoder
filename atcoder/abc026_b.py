# https://atcoder.jp/contests/abc026/tasks/abc026_b

import math
N = int(input())
R = [int(input()) for _ in range(N)]
R.sort(reverse=True)

ans = 0
for i in range(N):
    if i % 2:
        ans -= R[i] * R[i]
    else:
        ans += R[i] * R[i]

print(ans * math.pi)
