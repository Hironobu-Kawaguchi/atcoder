# https://atcoder.jp/contests/abc030/tasks/abc030_c

import bisect
N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flg = True
ans = 0
time = 0
while flg:
    idx = bisect.bisect_left(a, time)
    if idx == N:
        flg = False
        break
    time = a[idx] + X

    idx = bisect.bisect_left(b, time)
    if idx == M:
        flg = False
        break
    time = b[idx] + Y
    ans += 1

print(ans)
