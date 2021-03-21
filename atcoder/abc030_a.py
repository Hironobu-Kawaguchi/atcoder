# https://atcoder.jp/contests/abc030/tasks/abc030_a

import sys
readline = sys.stdin.buffer.readline
A, B, C, D = map(int, readline().split())

if B*C > D*A:
    print('TAKAHASHI')
elif B*C == D*A:
    print('DRAW')
else:
    print('AOKI')
