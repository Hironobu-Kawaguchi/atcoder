# https://atcoder.jp/contests/abc153/tasks/abc153_d

import math
H = int(input())
f = [1]
for i in range(40):
    f.append(f[-1]+2**(i+1))
tmp = int(math.log2(H))
print(f[tmp])
