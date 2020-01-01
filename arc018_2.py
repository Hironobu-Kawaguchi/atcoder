# https://atcoder.jp/contests/arc018/tasks/arc018_2

import itertools
import sys
readline = sys.stdin.buffer.readline

N = int(readline())
XY = [list(map(int, readline().split())) for _ in range(N)]

def chk(p, q, r):
    x = (q[0]-p[0]) * (r[1]-p[1]) - (q[1]-p[1]) * (r[0]-p[0])
    return x != 0 and x & 1 == 0

ans = sum(1 if chk(p,q,r) else 0 for p,q,r in itertools.combinations(XY, 3))
print(ans)
