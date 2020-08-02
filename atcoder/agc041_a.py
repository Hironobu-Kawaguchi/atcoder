# https://atcoder.jp/contests/agc041/tasks/agc041_a

import sys
readline = sys.stdin.buffer.readline

N, A, B = map(int, readline().split())
if (B-A)%2:
    ans = (B-A)//2 + min(A-1, N-B) + 1
else:
    ans = (B-A)//2
print(ans)
