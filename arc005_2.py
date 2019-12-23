# https://atcoder.jp/contests/arc005/tasks/arc005_2

x, y, W = input().split()
x = int(x) - 1
y = int(y) - 1
cs = [input() for _ in range(9)]

if 'R' in W:
    c = 1
elif 'L' in W:
    c = -1
else:
    c = 0
if 'D' in W:
    r = 1
elif 'U' in W:
    r = -1
else:
    r = 0

ans = ''
for i in range(4):
    ans += cs[y][x]
    if x == 0 and c == -1:
        c = 1
    elif x == 8 and c == 1:
        c = -1
    if y == 0 and r == -1:
        r = 1
    elif y == 8 and r == 1:
        r = -1
    x += c
    y += r

print(ans)
