# https://atcoder.jp/contests/abc089/tasks/abc089_c

import itertools
N = int(input())
d = {'M':0 ,'A':0 ,'R':0 ,'C':0 ,'H':0}
for i in range(N):
    S = input()
    if S[0] in d:
        d[S[0]] += 1

ans = 0
# 5C3=10通り試す
for i, j, k in itertools.combinations(d.keys(), 3):
    ans += d[i] * d[j] * d[k]

print(ans)
