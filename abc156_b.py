# https://atcoder.jp/contests/abc156/tasks/abc156_b

import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())

ans = 0
while N > 0:
    ans += 1
    N //= K

print(ans)
