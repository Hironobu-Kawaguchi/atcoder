# https://atcoder.jp/contests/abc317/tasks/abc317_e
# 幅優先探索 (BFS: breadth first search)

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque
# INF = 1001001001001
bad = ['#', '>', 'v', '<', '^']

H, W = map(int, input().split())
A = [input() for _ in range(H)]
# for y in range(H): print(A[y], file=sys.stderr)

OK = [[True] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if A[y][x] == '#':
            OK[y][x] = False
        elif A[y][x] == 'S':
            sy, sx = y, x
        elif A[y][x] == 'G':
            gy, gx = y, x
        elif A[y][x] == '>':
            OK[y][x] = False
            for xx in range(x+1, W):
                if A[y][xx] in bad:
                    break
                OK[y][xx] = False
        elif A[y][x] == 'v':
            OK[y][x] = False
            for yy in range(y+1, H):
                if A[yy][x] in bad:
                    break
                OK[yy][x] = False
        elif A[y][x] == '<':
            OK[y][x] = False
            for xx in range(x-1, -1, -1):
                if A[y][xx] in bad:
                    break
                OK[y][xx] = False
        elif A[y][x] == '^':
            OK[y][x] = False
            for yy in range(y-1, -1, -1):
                if A[yy][x] in bad:
                    break
                OK[yy][x] = False
# for y in range(H): print(OK[y], file=sys.stderr)

vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]
q = deque([(sy, sx, 0)])
dist = [[-1] * W for _ in range(H)]
dist[sy][sx] = 0

while q:
    y, x, n = q.popleft()
    if [gy, gx] == [y, x]:
        break
    for i in range(4):
        ny = y + vy[i]
        nx = x + vx[i]
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        elif OK[ny][nx] and dist[ny][nx] == -1:
            dist[ny][nx] = n+1
            q.append((ny, nx, n+1))

# for y in range(H): print(dist[y], file=sys.stderr)

print(dist[gy][gx])
