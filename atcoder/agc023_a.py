# https://atcoder.jp/contests/agc023/tasks/agc023_a

import collections
N = int(input())
A = list(map(int, input().split()))

cum = [0]
for i in range(N):
    cum.append(cum[-1]+A[i])
c = collections.Counter(cum)

ans = 0
for v in c.values():
    ans += (v*(v-1))//2

print(ans)
