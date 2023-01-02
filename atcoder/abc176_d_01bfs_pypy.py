# https://atcoder.jp/contests/abc176/tasks/abc176_d

import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import deque
from itertools import product
INF = 1001001001
DX = [ 1, 0,-1, 0]
DY = [ 0, 1, 0,-1]

H, W = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1; cw -= 1; dh -= 1; dw -= 1;
S = [input() for _ in range(H)]
visited = [[False]*W for _ in range(H)]
cost = [[INF]*W for _ in range(H)]
cost[ch][cw] = 0

que = deque()
que.appendleft((ch, cw))
while que:
    x, y = que.popleft()
    if visited[x][y]: continue
    visited[x][y] = True
    if x==dh and y==dw: break
    for dx, dy in zip(DX, DY):
        nx = x + dx
        ny = y + dy
        if nx<0 or nx>=H: continue
        if ny<0 or ny>=W: continue
        if S[nx][ny]=='#': continue
        cost[nx][ny] = min(cost[nx][ny], cost[x][y])
        que.appendleft((nx, ny))
    for i, j  in product(range(-2, 3), repeat=2):
        nx = x + i
        ny = y + j
        if nx<0 or nx>=H: continue
        if ny<0 or ny>=W: continue
        if S[nx][ny]=='#': continue
        if cost[nx][ny]<cost[x][y] + 1: continue
        cost[nx][ny] = min(cost[nx][ny], cost[x][y] + 1)
        que.append((nx, ny))

if visited[dh][dw]:
    print(cost[dh][dw])
else:
    print(-1)
