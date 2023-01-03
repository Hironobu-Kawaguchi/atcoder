# https://atcoder.jp/contests/typical90/tasks/typical90_bt

import sys
# input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

H, W = map(int, input().split())
c = [input() for _ in range(H)]
di = [ 1, 0,-1, 0]
dj = [ 0, 1, 0,-1]
visited = [[False]*W for _ in range(H)]

ans = 0

def dfs(i, j, d):
    global ans
    if i==si and j==sj:
        ans = max(ans, d)
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni<0 or ni>=H: continue
        if nj<0 or nj>=W: continue
        if c[ni][nj]=='#': continue
        if visited[ni][nj]: continue
        visited[ni][nj] = True
        dfs(ni, nj, d+1)
        visited[ni][nj] = False
    return

for si in range(H):
    for sj in range(W):
        if c[si][sj]=='#': continue
        dfs(si, sj, 0)

if ans>2:
    print(ans)
else:
    print(-1)
