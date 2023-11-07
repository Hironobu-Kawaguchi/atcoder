# https://atcoder.jp/contests/ahc024/tasks/ahc024_a

import os
import copy
from collections import deque
import time

start_time = time.time()
limit_time = 1.0
limit_time2 = 1.5

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

def input_c():
    global N
    C_original = [list(map(int, input().split())) for _ in range(N)]
    N += 2
    C = []
    for i in range(N):
        if i==0 or i==N-1:
            C.append([0]*N)
        else:
            C.append([0] + C_original[i-1] + [0])
    return C

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

C = input_c()
G = create_graph(C)
# print(G, file=os.sys.stderr)

def ok2zero(old_d, y, x):
    old_color = old_d[y][x]
    cnt_zero, cnt_old_color = 0, 0
    old_colors = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            ny = y + i
            nx = x + j
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if old_d[ny][nx]==old_color:
                cnt_old_color += 1
                if i!=0 or j!=0:
                    old_colors.append([(ny, nx)])
            elif old_d[ny][nx]==0:
                cnt_zero += 1
            else:
                return False
    if cnt_zero==0 or cnt_old_color==0:
        return False
    if cnt_old_color > 1:
        # old_colorsが連結しているか確認する
        visited = [[False]*N for _ in range(N)]
        q = deque(old_colors[0])
        while q:
            old_y, old_x = q.popleft()
            if visited[old_y][old_x]: continue
            visited[old_y][old_x] = True
            for k in range(4):
                ny = old_y + dy[k]
                nx = old_x + dx[k]
                if nx<0 or nx>=N or ny<0 or ny>=N: continue
                if nx<x-1 or nx>x+1 or ny<y-1 or ny>y+1: continue
                if nx==x and ny==y: continue
                if visited[ny][nx]: continue
                if old_d[ny][nx]==old_color:
                    q.append((ny, nx))
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                ny = y + i
                nx = x + j
                if nx<0 or nx>=N or ny<0 or ny>=N: continue
                if ny==y and nx==x: continue
                if old_d[ny][nx]==0: continue
                if visited[ny][nx]==False:
                    return False
    return True

def bfs_zero(old_c):
    # color=0と接しているマスで0にできるマスを変えていく
    visited = [[False]*N for _ in range(N)]
    q = deque([(0, 0)])
    while q and time.time() - start_time < limit_time2:
    # while q:
        y, x = q.popleft()
        if visited[y][x]: continue
        visited[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            if visited[ny][nx]: continue
            if old_c[ny][nx]==0:
                q.append((ny, nx))
            elif ok2zero(old_c, ny, nx):
                old_c[ny][nx] = 0
                # print("2zero", ny-1, nx-1, file=os.sys.stderr)
                q.append((ny, nx))
    return old_c

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
            if time.time() - start_time > limit_time: return False
            if visited[i][j]: continue
            # if new_d[i][j]==0: continue
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
        if time.time() - start_time > limit_time: return False
        if new_g[i] != G[i]:
            # print('ng', i, new_g[i], G[i], file=os.sys.stderr)
            return False
    return True

def remove_line(old_d):
    ret = old_d
    while time.time() - start_time < limit_time:
        for x in range(N):
            if time.time() - start_time > limit_time: break
            new_d = remove_line_x(ret, x)
            if ok(new_d):
                ret = new_d
                # print('ok x:', x, file=os.sys.stderr)
        for y in range(N):
            if time.time() - start_time > limit_time: break
            new_d = remove_line_y(ret, y)
            if ok(new_d):
                ret = new_d
                # print('ok y:', y, file=os.sys.stderr)
        for x in range(N-1, -1, -1):
            if time.time() - start_time > limit_time: break
            new_d = remove_line_x(ret, x)
            if ok(new_d):
                ret = new_d
                # print('ok x:', x, file=os.sys.stderr)
        for y in range(N-1, -1, -1):
            if time.time() - start_time > limit_time: break
            new_d = remove_line_y(ret, y)
            if ok(new_d):
                ret = new_d
                # print('ok y:', y, file=os.sys.stderr)
    return ret

def solve():
    ans = C
    print("time 01:", time.time() - start_time, file=os.sys.stderr)
    ans = remove_line(ans)
    print("time 02:", time.time() - start_time, file=os.sys.stderr)
    ans = bfs_zero(ans)
    print("time 03:", time.time() - start_time, file=os.sys.stderr)
    return ans

def main():
    ans = solve()
    for i in range(N):
        if i==0 or i==N-1: continue
        print(*ans[i][1:-1])
    return

main()
