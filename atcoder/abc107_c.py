# https://atcoder.jp/contests/abc107/tasks/abc107_c

import sys
input = sys.stdin.buffer.readline
INF = 1001001001

N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = INF

for i in range(N-K+1):
    if x[i] < 0:
        neg = -x[i]
    else:
        neg = 0
    if x[i+K-1] > 0:
        pos = x[i+K-1]
    else:
        pos = 0
    tmp = neg + pos + min(neg, pos)
    ans = min(ans, tmp)

print(ans)
