# D - 派閥
# https://atcoder.jp/contests/abc002/tasks/abc002_4

import itertools

# 形成した派閥を group として持つ
def dfs(i, group):
    global ans
    if i == n:
        # group 内の全員が知り合い同士か
        flag = True

        # group 内から2人選ぶ組み合わせのループ
        for i in itertools.combinations(group, 2):
            # 1人でも知り合いでなければ終了
            if friend[i[0]][i[1]] == 0:
                flag = False
                break

        if flag:
            ans = max(ans, len(group))

    else:
        dfs(i + 1, group)
        dfs(i + 1, group + [i])


n, m = map(int, input().split())
friend = [[0] * n for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    friend[x][y] = 1
    friend[y][x] = 1

ans = 0

dfs(0, [])
print(ans)