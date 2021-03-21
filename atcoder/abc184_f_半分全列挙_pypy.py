# https://atcoder.jp/contests/abc184/tasks/abc184_f

import bisect
n, t = map(int, input().split())
a = list(map(int, input().split()))

x, y = [0], [0]
for i in range(n):
    for j in range(len(x)):
        x.append(x[j]+a[i])
    x, y = y, x
x.sort()
ans = 0
for i in y:
    if i>t: continue
    j = bisect.bisect_right(x, t-i)
    ans = max(ans, i+x[j-1])
print(ans)
