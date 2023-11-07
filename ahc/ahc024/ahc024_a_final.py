# https://atcoder.jp/contests/ahc024/tasks/ahc024_a

import os
import copy
from collections import deque
import time

start_time = time.time()
limit_time = 1.0

N, M = map(int, input().split())
C_original = [list(map(int, input().split())) for _ in range(N)]
N += 2
C = []
for i in range(N):
    if i==0 or i==N-1:
        C.append([0]*N)
    else:
        C.append([0] + C_original[i-1] + [0])

# print(N, M, file=os.sys.stderr)
# for i in range(N):
#     print(*C[i], file=os.sys.stderr)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 隣接する色をグラフ化する
def create_graph(new_d):
    new_g = [set() for _ in range(M+1)]
    for i in range(N):
        for j in range(N):
            if i!=0:
                # if new_d[i][j]==0 or new_d[i-1][j]==0: continue
                if new_d[i][j]!=new_d[i-1][j]:
                    new_g[new_d[i][j]].add(new_d[i-1][j])
                    new_g[new_d[i-1][j]].add(new_d[i][j])
            if j!=0:
                # if new_d[i][j]==0 or new_d[i][j-1]==0: continue
                if new_d[i][j]!=new_d[i][j-1]:
                    new_g[new_d[i][j]].add(new_d[i][j-1])
                    new_g[new_d[i][j-1]].add(new_d[i][j])
    return new_g

G = create_graph(C)
# print(G, file=os.sys.stderr)

def remove_line_y(old_d, y):
    new_d = []
    for i in range(N):
        if i!=y:
            new_d.append(old_d[i])
    new_d.append([0]*N)
    return new_d

def remove_line_x(old_d, x):
    new_d = []
    for i in range(N):
        new_d.append(old_d[i][:x] + old_d[i][x+1:] + [0])
    return new_d

def connected_components(new_d):
    visited = [[False]*N for _ in range(N)]
    finishd = [False]*(M+1)
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            if new_d[i][j]==0: continue
            if finishd[new_d[i][j]]: continue
            finishd[new_d[i][j]] = True
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                visited[x][y] = True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=N: continue
                    if visited[nx][ny]: continue
                    if new_d[nx][ny]!=new_d[x][y]: continue
                    q.append((nx, ny))
    for i in range(N):
        for j in range(N):
            if new_d[i][j]==0: continue
            if not visited[i][j]:
                return False
    return True    

def ok(new_d):
    if not connected_components(new_d):
        return False
    new_g = create_graph(new_d)
    for i in range(1, M+1):
        if new_g[i] != G[i]:
            # print('ng', i, new_g[i], G[i], file=os.sys.stderr)
            return False
    return True

D = C
while time.time() - start_time < limit_time:
    for x in range(N):
        if time.time() - start_time > limit_time: break
        new_d = remove_line_x(D, x)
        if ok(new_d):
            D = new_d
            # print('ok x:', x, file=os.sys.stderr)
    for y in range(N):
        if time.time() - start_time > limit_time: break
        new_d = remove_line_y(D, y)
        if ok(new_d):
            D = new_d
            # print('ok y:', y, file=os.sys.stderr)

for i in range(N):
    if i==0 or i==N-1: continue
    print(*D[i][1:-1])
