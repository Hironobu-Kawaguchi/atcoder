# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

# 縦横それぞれが異なる2進数の差で表せればOK

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve():
    x, y = map(int, readline().split())
    mx = abs(x) + abs(y)
    # print(bin(mx), len(bin(mx)))
    keta = len(bin(mx)) - 2
    dx = [ 0, 0, 1,-1]
    dy = [ 1,-1, 0, 0]
    dr = ['N', 'S', 'E', 'W']
    for i in range(1<<(keta*2)):
        nowx, nowy = 0, 0
        for j in range(keta):
            d = (i>>(j*2))%4
            nowx += dx[d] * (1<<j)
            nowy += dy[d] * (1<<j)
        # print(nowx, nowy, j, d, i)
        if nowx == x and nowy == y:
            # print(i)
            break
    else:
        return "IMPOSSIBLE"
    ret = ''
    for j in range(keta):
        d = (i>>(j*2))%4
        ret += dr[d]
    return ret

T = int(readline())
for x in range(T):
    y = solve()
    print('Case #{}:'.format(x + 1), y)
