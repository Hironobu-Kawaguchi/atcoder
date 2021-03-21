# https://atcoder.jp/contests/abc107/tasks/abc107_b

H, W = map(int, input().split())
a = [input() for _ in range(H)]
yck = [1] * H
xck = [1] * W

for y in range(H):
    for x in range(W):
        if a[y][x] == '#':
            yck[y] = 0
            xck[x] = 0
for y in range(H):
    if yck[y]: continue
    ans = ''
    for x in range(W):
        if xck[x]: continue
        ans += a[y][x]
    print(ans)
