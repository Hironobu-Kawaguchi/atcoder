# https://atcoder.jp/contests/atc001/tasks/fft_c

import numpy as np

N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

fft_len = 2*10**5
x = np.fft.irfft(np.fft.rfft(A, fft_len) * np.fft.rfft(B, fft_len))

print(0)
for i in range(2*N-1):
    print(int(x[i]+0.5))
