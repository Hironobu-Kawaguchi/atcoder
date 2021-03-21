# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_b

from collections import defaultdict
N = int(input())
ABC = [input() for _ in range(3)]

ans = 0
for i in range(N):
    d = defaultdict(int)
    for j in range(3):
        d[ABC[j][i]] += 1
    ans += 3 - max(d.values())
print(ans)
