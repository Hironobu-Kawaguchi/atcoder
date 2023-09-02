# https://atcoder.jp/contests/ahc021/tasks/ahc021_a

import sys

N = 30
N2 = N*(N+1)//2
b = []
for i in range(N):
    b.extend(list(map(int, input().split())))
# for i in range(N2):
#     b[i] -= 1
# print(b, file=sys.stderr)

c = [-1] * N2
for i in range(N2):
    c[b[i]] = i
# print(c, file=sys.stderr)

xy = []
for x in range(N):
    for y in range(x+1):
        xy.append((x, y))
# print(xy, file=sys.stderr)

def xy2i(x, y):
    return x*(x+1)//2 + y

ans = []

def ball_swap(x1, y1, x2, y2):
    b[xy2i(x1, y1)], b[xy2i(x2, y2)] = b[xy2i(x2, y2)], b[xy2i(x1, y1)]
    c[b[xy2i(x1, y1)]], c[b[xy2i(x2, y2)]] = c[b[xy2i(x2, y2)]], c[b[xy2i(x1, y1)]]
    ans.append([x1, y1, x2, y2])
    # print(len(ans), ans[-1], b[xy2i(x1, y1)], file=sys.stderr)
    return

for i in range(N2):
    x, y = xy[c[i]]
    while x>0:
        nx = x-1
        if y==0:
            ny = 0
        elif y == x:
            ny = y-1
        elif b[xy2i(x-1, y-1)]>b[xy2i(x-1, y)]:
            ny = y-1
        else:
            ny = y
        if i > b[xy2i(nx, ny)]: break
        ball_swap(nx, ny, x, y)
        x, y = nx, ny

print(len(ans))
for x1, y1, x2, y2 in ans:
    print(x1, y1, x2, y2)
