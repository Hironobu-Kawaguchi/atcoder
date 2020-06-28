# https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_b

import sys
input = sys.stdin.buffer.readline
import numpy as np

D = int(input())
c = np.array(input().split(), dtype=np.int32)
s = np.array([input().split() for _ in range(D)], dtype=np.int32)
t = [int(input()) for _ in range(D)]
last = np.zeros(26, dtype=np.int32)
# print(s)
# print(s.shape)

ans = []
point = 0
for i in range(D):
    last[t[i]-1] = i+1
    down = (i+1-last)*c
    point += s[i, t[i]-1] - down.sum()
    print(point)
