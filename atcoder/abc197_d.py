# https://atcoder.jp/contests/abc197/tasks/abc197_d

import math

N = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())
xc = (x0 + xh) / 2
yc = (y0 + yh) / 2
xv = x0 - xc
yv = y0 - yc

theta = 2 * math.pi / N
x = xv * math.cos(theta) - yv * math.sin(theta) + xc
y = xv * math.sin(theta) + yv * math.cos(theta) + yc

print(x, y)

