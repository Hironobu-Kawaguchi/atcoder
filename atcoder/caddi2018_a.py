# https://atcoder.jp/contests/caddi2018/tasks/caddi2018_a

N, P = map(int, input().split())

from collections import defaultdict
d = defaultdict(int)
i = 2
while P >= i*i:
    if P%i==0:
        P //= i
        d[i] += 1
    elif i == 2:
        i += 1
    else:
        i += 2
if P != 1:
    d[P] += 1

ans = 1
for k, v in d.items():
    # print(k, v)
    if v >= N:
        ans *= k**(v//N)
    # z = v // N
    # ans *= k**z
print(ans)
