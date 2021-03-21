# https://atcoder.jp/contests/abc154/tasks/abc154_b

from collections import Counter
N = int(input())
A = list(map(int, input().split()))
c = Counter(A).values()
ans = "YES"
for v in c:
    if v > 1:
        ans = "NO"
print(ans)
