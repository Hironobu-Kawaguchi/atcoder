# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c

import numpy as np
H, W, K = map(int, input().split())

s = np.zeros((H, W), dtype=int)
num = 1
for i in range(H):
    _s = input()
    for j in range(W):
        if _s[j] == '#':
            s[i,j] = num
            num += 1
        else:
            s[i,j] = 0

flg = False
for i in range(H):
    if all(s[i,:] == 0):
        if flg:
            s[i,:] = s[i-1,:]
    else:
        flg = True
        prej = 0
        for j in range(W):
            if s[i, j] != 0:
                num = s[i, j]
                s[i, prej:j] = num
                prej = j+1
        else:
            s[i, prej:] = num

for i in range(H-1, -1, -1):
    if all(s[i,:] == 0):
        s[i,:] = s[i+1,:]
            
for i in range(H):
    ans = ''
    for j in range(W):
        ans += str(s[i, j]) + ' '
    print(ans)
