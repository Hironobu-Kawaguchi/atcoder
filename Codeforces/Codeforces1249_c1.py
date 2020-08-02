# https://codeforces.com/contest/1249/problem/C1
# Codeforces Round #595 (Div. 3)

# 3**9=19683>10**4 3**38=1350851717672992089>10**18

import bisect
import heapq
MAXP = 39

l = [0] * MAXP
for i in range(MAXP):
    l[i] = 3**i

h = []
for b in range(1<<MAXP):
    tmp = 0
    for i in range(MAXP):
        if b>>i&1:
            tmp += l[i]
    heapq.heappush(h, tmp)
print(h[-1])

q = int(input())
for i in range(q):
    n = int(input())
    ans = h[bisect.bisect_left(h, n)]
    print(ans)
