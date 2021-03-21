# https://atcoder.jp/contests/aising2019/tasks/aising2019_c

import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
check = [[0]*W for _ in range(H)]
di = [-1, 0, 1, 0]
dj = [ 0,-1, 0, 1]
black, white = 0, 0

def dfs(i, j):
    global check, black, white
    if check[i][j]:
        return
    else:
        check[i][j] = 1
    if S[i][j] == '#':
        black += 1
    else:
        white += 1
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni < 0 or ni >= H or nj < 0 or nj >= W: continue
        if S[i][j] == S[ni][nj]: continue
        dfs(ni, nj)
    return

ans = 0
for i in range(H):
    for j in range(W):
        black, white = 0, 0
        dfs(i, j)
        ans += black * white

print(ans)
