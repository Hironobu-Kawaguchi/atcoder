# https://atcoder.jp/contests/abc203/tasks/abc203_e

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# import copy
N, M = map(int, input().split())
xy = [[int(i) for i in input().split()] for _ in range(M)]
# xy.sort()
d = dict()
for x, y in xy:
    if x not in d:
        d[x] = [y]
    else:
        d[x].append(y)
# print(d)
now = set([N])
for x, lst in sorted(d.items()):
    # next = copy.copy(now)
    adds, rems = set(), set()
    for y in lst:
        rems.add(y)
        # if y in next:
        #     next.remove(y)
    for y in lst:
        if y-1 in now:
            adds.add(y)
            # next.add(y)
        if y+1 in now:
            adds.add(y)
            # next.add(y)
    now -= rems
    now |= adds
    # now = copy.copy(next)
    # print(x, now)
print(len(now))

