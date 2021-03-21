# https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_a
import sys
input = sys.stdin.buffer.readline
import numpy as np

D = int(input())
c = np.array(input().split(), dtype=np.int32)
s = np.array([input().split() for _ in range(D)], dtype=np.int32)
last = np.zeros(26, dtype=np.int32)
# print(s)
# print(s.shape)

ans = []
point = 0
for i in range(D):
    down = (i+1-last)*c
    loss = down * 5 + s[i,:]
    idx = np.argmax(loss)
    ans.append(idx+1)
    point += s[i, idx] - down.sum()
    last[idx] = i+1
    # print(loss)

for i in range(D):
    print(ans[i])


# print(point)  ### 3 78372 / 2447297 / 98149341
# print(point)  ### 4 78372 / 2462964 / 
print(point)    ### 5 78372 / 2565821 / 
# print(point)  ### 6 78372 / 2552338 / 
