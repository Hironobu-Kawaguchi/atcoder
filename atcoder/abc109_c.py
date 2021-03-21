# C - Skip
# https://atcoder.jp/contests/abc109/tasks/abc109_c

import fractions
N, X = map(int, input().split())
x = list(map(int, input().split()))
ans = abs(x[0] - X)
for i in range(1, N):
    ans = fractions.gcd(abs(x[i] - X), ans)
print(ans)
