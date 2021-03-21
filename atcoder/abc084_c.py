# https://atcoder.jp/contests/abc084/tasks/abc084_c

import math
N = int(input())
C, S, F = [], [], []
for i in range(N-1):
    _c, _s, _f = map(int, input().split())
    C.append(_c)
    S.append(_s)
    F.append(_f)

ans = [0] * N
for i in range(N-1):
    for j in range(i+1):
        ans[j] = max(S[i], math.ceil(ans[j]/F[i]) * F[i]) + C[i]

for i in range(N):
    print(ans[i])
