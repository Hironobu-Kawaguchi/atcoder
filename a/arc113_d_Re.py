# https://atcoder.jp/contests/arc113/tasks/arc113_d

MOD = 998244353

from itertools import product
N, M, K = map(int, input().split())
s = set()
for X in product(range(1,K+1), repeat=(N*M)):
    # print(X)
    ab = []
    for i in range(N):
        a = K
        for j in range(M):
            a = min(a, X[i*M+j])
        ab.append(a)
    for j in range(M):
        b = 0
        for i in range(N):
            b = max(b, X[i*M+j])
        ab.append(b)
    s.add(tuple(ab))
# for ab in sorted(s):
#     print(ab)
print(len(s)%MOD)

# ans = (K**N - (K-1)**N) + ((K-1)**N)*(K**M-1)
# print(ans)

