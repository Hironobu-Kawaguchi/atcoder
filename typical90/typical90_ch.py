# https://atcoder.jp/contests/typical90/tasks/typical90_ch
# bit全探索

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 1000000007

N, Q = map(int, input().split())
X, Y, Z, W = [], [], [], []
for qi in range(Q):
    x, y, z, w = map(int, input().split())
    X.append(x-1)
    Y.append(y-1)
    Z.append(z-1)
    W.append(w)

ans = 1
for i in range(60):
    cnt = 0
    for bi in range(1<<N):
        for qi in range(Q):
            w = W[qi]>>i&1
            x = bi>>X[qi]&1
            y = bi>>Y[qi]&1
            z = bi>>Z[qi]&1
            if x|y|z!=w: break
        else:
            cnt += 1
    ans *= cnt
    ans %= MOD
print(ans)
