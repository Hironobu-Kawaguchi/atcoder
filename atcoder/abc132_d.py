# https://atcoder.jp/contests/abc132/tasks/abc132_d

import math
N, K = map(int, input().split())
mod = 10**9+7

def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

comb = combinations_count(N, K)
# print(comb)

cnt = K
for i in range(min(K-1, N-K)):
    ans = combinations_count(K-1, i) * combinations_count(N-K+1, i+1) 
    comb -= ans
    ans %= mod
    print(ans)
    cnt -= 1

print(comb % mod)
cnt -= 1

if cnt != 0:
    for i in range(cnt):
        print(0)


l = [0] * K
import itertools
for v in itertools.combinations(range(N), K):
    # print(v)
    vcnt = 1
    for i in range(len(v)-1):
        if v[i+1] != v[i] + 1:
            vcnt += 1
    # print(vcnt)
    l[vcnt-1] += 1

for i in range(K):
    print(l[i] % mod)
