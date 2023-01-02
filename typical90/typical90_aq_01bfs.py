# https://atcoder.jp/contests/typical90/tasks/typical90_aq

import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import deque
INF = 1001001001

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1; cs -= 1; rt -= 1; ct -= 1
S = [input() for _ in range(H)]

dx = [ 1, 0,-1, 0]
dy = [ 0, 1, 0,-1]
cost = [[[INF]*4 for _ in range(W)] for _ in range(H)]
que = deque()
for i in range(4):
    cost[rs][cs][i] = 0
    que.append([rs, cs, i])

while que:
    x, y, d = que.pop()
    if x==rt and y==ct:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=H: continue
        if ny<0 or ny>=W: continue
        if S[nx][ny]=='#': continue
        if cost[nx][ny][i]<=cost[x][y][i]: continue
        if i==d:
            que.append([nx, ny, i])
            cost[nx][ny][i] = min(cost[nx][ny][i], cost[x][y][d])
            for j in range(4):
                if i!=j:
                    cost[nx][ny][j] = min(cost[nx][ny][j], cost[x][y][d] + 1)
        else:
            que.appendleft([nx, ny, i])
            cost[nx][ny][i] = min(cost[nx][ny][i], cost[x][y][d] + 1)
            for j in range(4):
                if i!=j:
                    cost[nx][ny][j] = min(cost[nx][ny][j], cost[x][y][d] + 2)
ans = INF
for i in range(4):
    ans = min(ans, cost[rt][ct][i])
# for i in range(4):
#     for x in range(H):
#         print()
#         for y in range(W):
#             print(cost[x][y][i], end='\t')
print(ans)
