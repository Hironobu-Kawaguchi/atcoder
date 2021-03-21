# https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_c

import numpy as np
import sys
input = sys.stdin.readline

N,X = map(int,input().split())
A = np.array(input().split(), dtype=np.int64)

B = np.where(A==-1,0,A)
xor = np.bitwise_xor.reduce(B)
empty = (A==-1).sum()

if empty == 0:
    flg = (xor == X)
    answer = A
elif empty == 1:
    x = xor^X
    flg = (x <= X)
    answer = A.copy()
    answer[A==-1] = x
else:
    x = int(xor ^ X)
    # print(bin(x), bin(xor), bin(X))
    I = np.where(A==-1)
    answer = B.copy()
    i,j = I[0][:2]
    # print(I, i, j)
    n = 1<<(x.bit_length()-1) if x else 0
    m = n^x
    # print(bin(n), bin(m))
    answer[i] = n
    answer[j] = m
    flg = (n <= X)
    # print(np.bitwise_xor.reduce(answer))

if not flg:
    print(-1)
else:
    print(' '.join(answer.astype(str)))
