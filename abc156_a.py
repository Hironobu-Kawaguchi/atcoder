# https://atcoder.jp/contests/abc156/tasks/abc156_a

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, R = map(int, input().split())

ans = R
if N < 10:
    ans += 100 * (10-N)
print(ans)
