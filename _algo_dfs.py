# A - 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a

# pythonだとデフォルトの再帰処理回数の上限に引っかかってしまうので、それを変更
import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    d[x][y] = 1

    # 移動4方向をループ
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # nx と ny が街の範囲内か、行ったことがないか、塀ではないかを判定
        if 0 <= nx and nx < n and 0 <= ny and ny < m and d[nx][ny] == 0 and c[nx][ny] != "#":
                dfs(nx, ny)


n, m = map(int, input().split())
c = [list(input()) for i in range(n)]

# 到達したかどうか（0は未到達、1は到達済み）
d = [[0] * m for i in range(n)]

# 移動する4方向
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# スタート地点から dfs を始める
for i in range(n):
    for j in range(m):
        if c[i][j] == "s":
            dfs(i, j)

# ゴール地点に到達したかどうか
for i in range(n):
    for j in range(m):
        if c[i][j] == "g" and d[i][j]:
            print("Yes")
            exit()
print("No")