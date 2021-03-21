# https://atcoder.jp/contests/abc144/tasks/abc144_d

import math
a, b, x = map(int, input().split())
if x <= a*a*b//2:
    ans = 90 - math.degrees(math.atan(2*x/(a*b*b)))
else:
    ans = math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
print(ans)
