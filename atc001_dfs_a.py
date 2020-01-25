# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
c = [input() for _ in range(H)]
dx = [-1, 0, 1, 0]
dy = [ 0,-1, 0, 1]
reached = [[False]*W for _ in range(H)]

def dfs(x, y):
    # global reached
    if (x<0 or x>=W or y<0 or y>=H or c[y][x]=='#'): return
    if (reached[y][x]): return
    reached[y][x] = True
    for dir in range(4):
        dfs(x+dx[dir], y+dy[dir])
    return

for y in range(H):
    for x in range(W):
        if c[y][x] == 's':
            sy = y
            sx = x
        if c[y][x] == 'g':
            gy = y
            gx = x
dfs(sx, sy)
if reached[gy][gx]:
    print("Yes")
else:
    print("No")
