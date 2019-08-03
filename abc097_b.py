# https://atcoder.jp/contests/abc097/tasks/abc097_b

import math
N = int(input())

s = set([1])
for b in range(2, int(math.sqrt(N))+1):
    p = 2
    while b**p <= N:
        s.add(b**p)
        p += 1

ans = max(s)
print(ans)
