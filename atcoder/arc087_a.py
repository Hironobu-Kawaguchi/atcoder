# https://atcoder.jp/contests/abc082/tasks/arc087_a

import collections
N = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)
ans = 0
for i in c:
    if c[i] > i:
        ans += c[i] - i
    elif c[i] < i:
        ans += c[i]

print(ans)
