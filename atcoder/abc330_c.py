# https://atcoder.jp/contests/abc330/tasks/abc330_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import math
INF = 10**18
D = int(input())

ans = INF
x = 0
while x*x <= D:
    y = int((D - x*x)**0.5)
    ans = min(ans, abs(D - x*x - y*y))
    ans = min(ans, abs(D - x*x - (y+1)*(y+1)))
    x += 1
print(ans)
