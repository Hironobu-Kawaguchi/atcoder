# https://atcoder.jp/contests/abc146/tasks/abc146_c

import math
A, B, X = map(int, input().split())

left = 0
right = 10**9+1

while left + 1 < right:
    tmp = (left + right) // 2
    if tmp * A + int(math.log10(tmp)+1) * B <= X:
        left = tmp
    else:
        right = tmp

ans = left
print(ans)
