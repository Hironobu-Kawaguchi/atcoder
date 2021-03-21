# https://atcoder.jp/contests/donuts-2015/tasks/donuts_2015_1

import math
r, d = map(int, input().split())
ans = 2*d*math.pi * r*r*math.pi
print(ans)
