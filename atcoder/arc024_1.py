# https://atcoder.jp/contests/arc024/tasks/arc024_1

from collections import Counter

L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
cl = Counter(l)
cr = Counter(r)

ans = 0
for k in cl.keys():
    ans += min(cl[k], cr[k])

print(ans)
