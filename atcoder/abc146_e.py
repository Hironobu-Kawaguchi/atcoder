# https://atcoder.jp/contests/abc146/tasks/abc146_e

from queue import Queue
from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
s = [0] * (n+1)
for i in range(n):
    s[i+1] = (s[i]+a[i])%k

d = defaultdict(int)
ans = 0
q = Queue()

for j in range(n+1):
    ans += d[s[j]]
    d[s[j]] += 1
    q.put(s[j])
    if q.qsize() == k:
        d[q.get()] -= 1

print(ans)
