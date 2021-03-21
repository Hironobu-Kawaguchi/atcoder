# https://atcoder.jp/contests/arc035/tasks/arc035_b

from collections import Counter
MOD = 10**9+7
f = [1]
for i in range(10000):
    f.append(f[-1]*(i+1)%MOD)

N = int(input())
T = [int(input()) for _ in range(N)]
T.sort()

ans1 = 0
cum = 0
for i in range(N):
    cum += T[i]
    ans1 += cum
print(ans1)

ans2 = 1
for v in Counter(T).values():
    ans2 *= f[v]
    ans2 %= MOD
print(ans2)
