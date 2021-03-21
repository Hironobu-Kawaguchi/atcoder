# B - 埋め立て
# https://atcoder.jp/contests/arc031/tasks/arc031_2

def dfs(x, y):
    field[x][y] = "x"

    # 移動4方向をループ
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # nx と ny が地図の範囲内か、field[nx][ny]が島か判定
        if 0 <= nx and nx < 10 and 0 <= ny and ny < 10 and field[nx][ny] == "o":
                dfs(nx, ny)


A = [list(input()) for i in range(10)]

# 移動する4方向
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 埋め立てる1マスを全探索
for p in range(10):
    for q in range(10):
        if A[p][q] == "x":
            # 海だったら A を field にコピーしてそのマスを埋め立てる
            field = [k[:] for k in A]
            field[p][q] = "o"
            count = 0
            # 埋め立てた上で dfs で島の数をカウント
            for i in range(10):
                for j in range(10):
                    if field[i][j] == "o":
                        dfs(i, j)
                        count += 1
            # count (島の数)が1かどうか
            if count == 1:
                print("YES")
                exit()
print("NO")
