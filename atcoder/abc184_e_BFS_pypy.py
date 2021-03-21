# https://atcoder.jp/contests/abc184/tasks/abc184_e

from collections import deque
from string import ascii_lowercase
ascii = dict([[v, i] for i, v in enumerate(ascii_lowercase)])
INF = 1001001001
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

H, W = map(int, input().split())
a = [input() for _ in range(H)]
dist = [[INF]*W for _ in range(H)]
warps = [list() for _ in range(26)]
q = deque()
for i in range(H):
    for j in range(W):
        if a[i][j] == 'S':
            q.append((i,j))
            dist[i][j] = 0
        if a[i][j].islower():
            warps[ascii[a[i][j]]].append((i,j))
ans = -1
while q:
    i, j = q.popleft()
    if  a[i][j] == 'G':
        ans = dist[i][j]
        break
    for v in range(4):
        ni = i + di[v]
        nj = j + dj[v]
        if ni<0 or ni>=H: continue
        if nj<0 or nj>=W: continue
        if a[ni][nj] == '#': continue
        if dist[ni][nj] != INF: continue
        dist[ni][nj] = dist[i][j] + 1
        q.append((ni,nj))
    if a[i][j].islower():
        for ni, nj in warps[ascii[a[i][j]]]:
            if ni<0 or ni>=H: continue
            if nj<0 or nj>=W: continue
            if a[ni][nj] == '#': continue
            if dist[ni][nj] != INF: continue
            dist[ni][nj] = dist[i][j] + 1
            q.append((ni,nj))
        warps[ascii[a[i][j]]].clear()
print(ans)
