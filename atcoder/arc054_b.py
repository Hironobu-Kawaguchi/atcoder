# https://atcoder.jp/contests/arc054/tasks/arc054_b
# x + P * 2**(-x/1.5) の最大値 -> 微分 1 - 2/3 * P * log2 * 2**(-x/1.5) = 0
# 2**(-x/1.5) = 3/(2Plog2) -> -x/1.5 = log2(3/(2Plog2)) = log(3/(2Plog2))/log(2)
# x = -1.5 * log(3/(2Plog2))/log(2)

import math
P = float(input())
x = -1.5 * math.log(3/(2*P*math.log(2)))/math.log(2)
if x > 0:
    print(x + P*(2**(-x/1.5)))
else:
    print(P)
