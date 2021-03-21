# https://atcoder.jp/contests/abc112/tasks/abc112_d

import math
N, M = map(int, input().split())

div = M
for i in range(1, int(math.sqrt(M))+1):
    if M % i:
        continue
    i2 = M // i
    if i >= N:
        div = min(div, i)
    if i2 >= N:
        div = min(div, i2)

print(M//div)
