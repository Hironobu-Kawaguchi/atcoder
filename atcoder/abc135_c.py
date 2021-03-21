# https://atcoder.jp/contests/abc135/tasks/abc135_c

import sys
input = sys.stdin.buffer.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] >= B[i]:
        ans += B[i]
    else:
        ans += A[i]
        tmp = min(B[i]-A[i], A[i+1])
        ans += tmp
        A[i+1] -= tmp
print(ans)
