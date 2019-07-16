# A - Darker and Darker
# https://atcoder.jp/contests/agc033/tasks/agc033_a

import numpy as np

H,W = map(int,input().split())
A = []
for i in range(H):
    A.append([0 if i == "#" else H + W for i in list(input())])
A = np.array(A)

for i in range(H-1):
  A[i+1, :] = np.minimum(A[i, :] + 1, A[i+1, :])
for i in range(H-1,0,-1):
  A[i-1,:] = np.minimum(A[i,:]+1,A[i-1,:])
for i in range(W-1):
  A[:,i+1] = np.minimum(A[:,i]+1,A[:,i+1])
for i in range(W-1,0,-1):
  A[:,i-1] = np.minimum(A[:,i]+1,A[:,i-1])
print(np.max(A))

"""
from collections import deque
H, W = map(int, input().split())
cs = []
q = deque()
s = set()
for h in range(H):
    cs.append(input())
    for w in range(W):
        if cs[h][w] == '#':
            s.add((h+1, w+1))
            q.append((h+1, w+1, 0))
vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]
ans = 0
# while len(s) < H * W:
# while len(q) > 0:
while q:
    y, x, n = q.popleft()
    for i in range(4):
        ny = y + vy[i]
        nx = x + vx[i]
        if ny >= 1 and ny <= H and nx >= 1 and nx <= W:
            if cs[ny-1][nx-1] == '.' and ((ny, nx) not in s):
                s.add((ny, nx))
                q.append((ny, nx, n+1))
                ans = max(ans, n+1)
print(ans)
"""

"""
H, W = map(int, input().split())
ans = 0
blk = []
for h in range(H):
    line = input()
    for w in range(W):
        if line[w] == '#':
            blk.append([h+1, w+1])
for h in range(H):
    for w in range(W):
        tmp = H + W
        if line[w] == '.':
            for y, x in blk:
                tmp = min(abs(h+1 - y) + abs(w+1 - x), tmp)
            ans = max(tmp, ans)
print(ans)
"""
