# https://codeforces.com/contest/1249/problem/C2
# Codeforces Round #595 (Div. 3)

# 3**9=19683>10**4 3**38=1350851717672992089>10**18

import bisect
MAXP = 19

l = [0] * MAXP
for i in range(MAXP):
    l[i] = 3**i

s = set()
for b in range(1<<MAXP):
    tmp = 0
    for i in range(MAXP):
        if b>>i&1:
            tmp += l[i]
    s.add(tmp)
goodlist = sorted(list(s))
# print(goodlist)

q = int(input())
for i in range(q):
    n = int(input())
    ans = goodlist[bisect.bisect_left(goodlist, n)]
    print(ans)
