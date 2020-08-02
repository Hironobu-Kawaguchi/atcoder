# https://atcoder.jp/contests/arc001/tasks/arc001_1

from collections import Counter
N = int(input())
c = input()
cntd = Counter(c)

mx, mn = 0, 100
for i in range(1, 5):
    mx = max(mx, cntd[str(i)])
    mn = min(mn, cntd[str(i)])

print(mx, mn)
