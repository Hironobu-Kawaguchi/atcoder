# https://atcoder.jp/contests/abc135/tasks/abc135_d

import numpy as np
import math
import itertools
# S = input()
mod = 10**9 + 7

for S in itertools.product(['?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=4):
    ans = 0
    # n = np.zeros(len(S), dtype=int)
    n = []
    chk = []
    for i in range(len(S)):
        if S[i] == '?':
            chk.append(i)
            n.append('0')
        else:
            # n[i] = int(S[i])
            n.append(S[i])

    if len(chk) == 0:
        break
    elif chk[0] == 0:
        # uso = math.ceil((10**(len(chk))-6) / 13)
        uso = math.ceil((10**(len(chk))-6) / 13)
    else:
        # uso = math.ceil((10**(len(chk))-1) / 13)
        uso = math.ceil((10**(len(chk))-1) / 13)
    amari = int(''.join(list(n))) % 13


    sums = np.zeros([len(chk), 10], dtype=int) 
    for a in itertools.product(range(10), repeat=len(chk)):
        for i, j in enumerate(a):
            n[chk[i]] = str(j)
        # print(n)
        num = int(''.join(list(n)))
        if num % 13 == 5:
            ans += 1
            # print(num)
            for i, j in enumerate(a):
                n[chk[i]] = str(j)
                sums[i, j] += 1

    if ans > uso:
        print(S, ans, uso, amari)

# print(chk)
# print(sums)
# print(ans % mod)

# print('uso:{}'.format(uso))
# print(amari)