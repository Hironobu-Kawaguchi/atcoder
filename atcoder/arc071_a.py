# https://atcoder.jp/contests/abc058/tasks/arc071_a

import string
import collections

n = int(input())
d = dict(zip(list(string.ascii_lowercase), [50]*26))
# print(d)

for _ in range(n):
    c = collections.Counter(input())
    for a in list(string.ascii_lowercase):
        d[a] = min(d[a], c[a])

ans = ''
for a in list(string.ascii_lowercase):
    ans += a * d[a]

print(ans)
