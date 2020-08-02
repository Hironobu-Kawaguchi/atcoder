# https://atcoder.jp/contests/abc057/tasks/abc057_c

import math
N = int(input())
num = int(N**0.5)
flg = True
while flg:
    if N % num == 0:
        ans = int(math.log10(N//num)) + 1
        flg = False
    else:
        num -= 1
print(ans)
