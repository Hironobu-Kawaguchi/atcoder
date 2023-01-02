# C - 器物損壊！高橋君
# https://atcoder.jp/contests/arc005/tasks/arc005_3

# 01-bfs
from collections import deque

def main():
    H, W = map(int, input().split())
    c = [list(input()) for i in range(H)]
    # print(c)
    cnt = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False]*W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if c[i][j] == "s":
                sx = i
                sy = j
                visited[i][j] = True
            if c[i][j] == "g":
                gx = i
                gy = j
    que = deque([])
    # 3つ目は壊した回数
    que.append((sx, sy, 0))

    while que:
        x, y, cost = que.pop()
        visited[x][y] = True
        if x==gx and y==gy:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=H: continue
            if ny<0 or ny>=W: continue
            if visited[nx][ny]: continue
            if c[nx][ny]=='#':
                if cost>=2:
                    continue
                else:
                    que.appendleft((nx, ny, cost + 1))
            else:
                que.append((nx, ny, cost))

    if visited[gx][gy]:
        print("YES")
    else:
        print("NO")
    return

main()



# from collections import deque

# def dfs():
#     d = [[[False] * 3 for j in range(w)] for i in range(h)]

#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]

#     for i in range(h):
#         for j in range(w):
#             if maze[i][j] == "s":
#                 sx = i
#                 sy = j
#             if maze[i][j] == "g":
#                 gx = i
#                 gy = j

#     que = deque([])
#     # 3つ目は壊した回数
#     que.append((sx, sy, 0))
#     # 座標と壊した回数ごとに行ける行けないを持つ
#     d[sx][sy][0] = True

#     while que:
#         # ここが popleft ではなく pop になっているためスタックになり、これはDFSです
#         p = que.pop()
#         if p[0] == gx and p[1] == gy:
#             break
#         for i in range(4):
#             nx = p[0] + dx[i]
#             ny = p[1] + dy[i]
#             t = p[2]

#             if not (0 <= nx and nx < h and 0 <= ny and ny < w):
#                 continue
#             # すでに2回壊してる状態で壁に当たると進めない
#             if t == 2 and maze[nx][ny] == "#":
#                 continue
#             if d[nx][ny][t]:
#                 continue
#             # 壁なら壊して進む
#             if maze[nx][ny] == "#":
#                 que.append((nx, ny, t + 1))
#                 d[nx][ny][t + 1] = True
#             else:
#                 que.append((nx, ny, t))
#                 d[nx][ny][t] = True

#     # ゴールの座標を壊した回数でループ
#     for i in range(3):
#         if d[gx][gy][i]:
#             return True


# h, w = map(int, input().split())
# maze = [list(input()) for i in range(h)]

# if dfs():
#     print("YES")
# else:
#     print("NO")