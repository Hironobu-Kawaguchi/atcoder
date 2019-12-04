# https://atcoder.jp/contests/abc027/tasks/abc027_c

import math
N = int(input())
d = int(math.log2(N))

i = 0
x = 1
if d % 2:
    while x <= N:
        if i % 2:
            x = x*2 + 1
        else:
            x = x*2
        i += 1
else:
    while x <= N:
        if i % 2:
            x = x*2
        else:
            x = x*2 + 1
        i += 1

if i % 2 or i == 0:
    print("Aoki")
else:
    print("Takahashi")
