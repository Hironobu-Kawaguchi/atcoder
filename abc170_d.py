# https://atcoder.jp/contests/abc170/tasks/abc170_d

import numpy as np
import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, (input().split())))
A.sort()
cnt = np.zeros(10**6+10, dtype=np.int32)
for x in A:
    if cnt[x] != 0:
        cnt[x] = 2
        continue
    cnt[x::x] += 1
ans = 0
for x in A:
    if cnt[x] == 1:
        ans += 1
print(ans)
