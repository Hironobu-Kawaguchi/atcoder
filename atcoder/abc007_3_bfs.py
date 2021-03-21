# C - 幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque
dx = [-1, 0, 1, 0]
dy = [ 0,-1, 0, 1]

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]

d = [[-1]*C for _ in range(R)]
d[sy-1][sx-1] = 0
q = deque([(sy-1, sx-1)])
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx<0 or nx>=C or ny<0 or ny>=R: continue
        if c[ny][nx] == '#':               continue
        if d[ny][nx] != -1:                continue
        d[ny][nx] = d[y][x] + 1
        if ny == gy-1 and nx == gx-1:
            break
        q.append((ny, nx))

print(d[gy-1][gx-1])


# from collections import deque

# def bfs():
#     d = [[float("inf")] * c for i in range(r)]

#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]

#     que = deque([])
#     que.append((sy, sx))
#     d[sy][sx] = 0

#     while que:
#         p = que.popleft()
#         if p[0] == gy and p[1] == gx:
#             break
#         for i in range(4):
#             nx = p[0] + dx[i]
#             ny = p[1] + dy[i]

#             if 0 <= nx and nx < r and 0 <= ny and ny < c and\
#                 maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
#                 que.append((nx, ny))
#                 d[nx][ny] = d[p[0]][p[1]] + 1

#     return d[gy][gx]


# r, c = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# sx -= 1
# sy -= 1
# gy -= 1
# gx -= 1
# maze = [list(input()) for i in range(r)]

# print(bfs())