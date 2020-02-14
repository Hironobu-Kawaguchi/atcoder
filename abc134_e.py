# https://atcoder.jp/contests/abc134/tasks/abc134_e

import sys
input = sys.stdin.readline
from collections import deque
import bisect

N = int(input())
A = [int(input()) for _ in range(N)]
A.reverse()

d = []
for i in range(N):
    p = bisect.bisect_right(d, A[i])
    if p==len(d):
        d.append(A[i])
    else:
        d[p] = A[i]
ans = len(d)
print(ans)
