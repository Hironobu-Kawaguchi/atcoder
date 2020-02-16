# https://atcoder.jp/contests/abc155/tasks/abc155_c

from collections import defaultdict
N = int(input())
S = [input() for _ in range(N)]
d = defaultdict(int)
maxn = 0

for i in range(N):
    d[S[i]] += 1
    maxn = max(maxn, d[S[i]])

for k, v in d.items():
    if v == maxn:
        print(k)
