# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

d = [[0]*3010 for _ in range(3010)]
for i in range(3010):
    for j in range(3010):
        d[i][j] = abs(i-1000) + abs(j-1000)

def solve():
    x, y, m = input().split()
    x = int(x)
    y = int(y)
    n = len(m)
    now_x = x + 1000
    now_y = y + 1000
    if d[now_x][now_y] == 0:
        return 0
    dir = {'N': (0,1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    for i in range(n):
        now_x += dir[m[i]][0]
        now_y += dir[m[i]][1]
        if d[now_x][now_y] <= i+1:
            # print(now_x, now_y, d[now_x][now_y], i)
            return i+1
    else:
        return "IMPOSSIBLE"

T = int(input())
for x in range(T):
    y = solve()
    print('Case #{}:'.format(x + 1), y)
