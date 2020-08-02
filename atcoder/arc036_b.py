# https://atcoder.jp/contests/arc036/tasks/arc036_b

import sys
input = sys.stdin.buffer.readline
N = int(input())
h = [int(input()) for _ in range(N)]

ans = 0
west, east = 0, 0
for i in range(N-1):
    if h[i] < h[i+1]:
        if east != 0:
            ans = max(ans, west + east + 1)
            west, east = 0, 0
        west += 1
    else:
        east += 1
ans = max(ans, west + east + 1)
print(ans)
