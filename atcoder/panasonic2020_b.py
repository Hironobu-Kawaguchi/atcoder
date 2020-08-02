# https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
else:
    ans = ((H+1)//2)*((W+1)//2) + (H//2)*(W//2)
print(ans)
