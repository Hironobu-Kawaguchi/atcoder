# https://atcoder.jp/contests/agc035/tasks/agc035_a

import collections
N = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)
v = list(c.values())
k = list(c.keys())

if 0 in c and c[0] == N:
    print('Yes')
elif len(c) == 2 and 0 in c and c[0] == N/3:
    print('Yes')
elif len(c) == 3 and v[0]==v[1]==v[2] and k[0]^k[1]^k[2] == 0:
    print('Yes')
else:
    print('No')
