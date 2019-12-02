# https://atcoder.jp/contests/abc094/tasks/arc095_b

import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()

ai = a[-1]
j = bisect.bisect(a, ai/2)
if abs(ai/2 - a[j]) < abs(ai/2 - a[j-1]):
    aj = a[j]
else:
    aj = a[j-1]

print(ai, aj)
