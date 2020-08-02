# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_g

import fractions

N = int(input())
# A, B = [], []
# s = set()
for i in range(N):
    a, b = map(int, input().split())
    # A.append(_a)
    # B.append(_b)
    ans = fractions.gcd(a, b)
    print(ans)
