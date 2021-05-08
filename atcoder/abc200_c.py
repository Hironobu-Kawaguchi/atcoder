# https://atcoder.jp/contests/abc200/tasks/abc200_c

from collections import Counter
n = int(input())
a = list(map(int, (input().split())))
for i in range(n):
    a[i] %= 200
cnt = Counter(a)
ans = 0
for i, v in cnt.items():
    if v>=2:
        ans += v*(v-1) // 2
print(ans)

