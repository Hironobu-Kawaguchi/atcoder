# D - 派閥
# https://atcoder.jp/contests/abc002/tasks/abc002_4

import itertools

n, m = map(int, input().split())
friend = [[0] * n for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    friend[x][y] = 1
    friend[y][x] = 1

ans = 0

for bit in range(1 << n):
    group = []

    for i in range(n):
        if bit & (1 << i):
            group.append(i)

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

print(ans)