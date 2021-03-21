# https://atcoder.jp/contests/abc010/tasks/abc010_3

import math
txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())

ans = "NO"
for i in range(n):
    x, y = map(int, input().split())
    if math.sqrt((txa - x)**2 + (tya - y)**2) + math.sqrt((txb - x)**2 + (tyb - y)**2) <= T * V:
        ans = "YES"

print(ans)
