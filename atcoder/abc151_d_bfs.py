# https://atcoder.jp/contests/abc151/tasks/abc151_d

from collections import deque
INF = 1001001001
di = [-1, 0, 1, 0]
dj = [ 0,-1, 0, 1]

H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for si in range(H):
    for sj in range(W):
        if S[si][sj] == '#': continue
        dist = [[INF] * W for _ in range(H)]
        dist[si][sj] = 0
        q = deque([(si, sj)])
        while q:
            i, j = q.popleft()
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]
                if (ni<0 or ni>=H or nj<0 or nj>=W): continue
                if S[ni][nj] == '#': continue
                if dist[ni][nj] != INF: continue
                dist[ni][nj] = dist[i][j] + 1
                q.append([ni, nj])
        for i in range(H):
            for j in range(W):
                if dist[i][j] == INF: continue
                ans = max(ans, dist[i][j])
print(ans)
