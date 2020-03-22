# https://atcoder.jp/contests/arc042/tasks/arc042_b
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

import math

x, y = map(int, input().split())
N = int(input())

node = []
for i in range(N):
    _x, _y = map(int, input().split())
    rad = math.atan2(_y-y, _x-x)
    node.append((rad, _x-x, _y-y))
node.sort()
# print(node)
node.append(node[0])

ans = 1001001.
for i in range(N):
    tmp1 = abs(node[i][1]*node[i+1][2] - node[i+1][1]*node[i][2])
    tmp2 = math.sqrt((node[i][1]-node[i+1][1])**2 + (node[i][2]-node[i+1][2])**2)
    ans = min(ans, tmp1/tmp2)
print(ans)
