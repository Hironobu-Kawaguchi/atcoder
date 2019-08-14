# https://atcoder.jp/contests/abc047/tasks/abc047_b

import numpy as np
W, H, N = map(int, input().split())
colors = np.ones((W, H), np.int)
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        colors[:x, :] = 0
    elif a == 2:
        colors[x:, :] = 0
    elif a == 3:
        colors[:, :y] = 0
    elif a == 4:
        colors[:, y:] = 0
ans = colors.sum()
# print(colors)
print(ans)
