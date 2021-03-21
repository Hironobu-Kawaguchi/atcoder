# https://atcoder.jp/contests/arc052/tasks/arc052_b
# 半径の2乗の累積和を作る

import sys
import math
input = sys.stdin.buffer.readline

MAX_X = 10010
r2 = [0] * MAX_X
r2_cum = [0] * MAX_X

N, Q = map(int, input().split())
for i in range(N):
    x, r, h = map(int, input().split())
    for j in range(h):
        r2[x+j] += (r**2) * h * ((((h-j)/h)**3) - ((h-1-j)/h)**3)
for x in range(MAX_X-1):
    r2_cum[x+1] = r2_cum[x] + r2[x]

for i in range(Q):
    a, b = map(int, input().split())
    ans = r2_cum[b] - r2_cum[a]
    ans *= math.pi
    ans /= 3
    print(ans)
