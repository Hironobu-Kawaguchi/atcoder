# C - Switches
# https://atcoder.jp/contests/abc128/tasks/abc128_c

import itertools

N, M = map(int, input().split())
k, s = [], []

for i in range(M):
    tmp = [int(j) for j in input().split()]
    k.append(tmp[0])
    s.append(tmp[1:])
p = [int(j) for j in input().split()]

ans = 0

for switch in itertools.product(range(2), repeat=N):
    flg = True
    for i in range(M):
        snum = 0
        for j in range(k[i]):
            if switch[s[i][j]-1]:
                snum += 1
        if snum % 2 == p[i]:
            continue
        else:
            flg = False
            break
    if flg:
        ans += 1

print(ans)
