# https://atcoder.jp/contests/abc182/tasks/abc182_d

import bisect
H, W, N, M = map(int, input().split())
yoko_block = [[-1,W] for _ in range(H)]
tate_block = [[-1,H] for _ in range(W)]
light = []
for i in range(N):
    a, b = map(int, input().split())
    light.append((a-1,b-1))
for i in range(M):
    c, d = map(int, input().split())
    bisect.insort(yoko_block[c-1], d-1)
    bisect.insort(tate_block[d-1], c-1)

yoko_set = set()
tate_set = set()
for i in range(N):
    x = bisect.bisect(yoko_block[light[i][0]], light[i][1])
    yoko_set.add((light[i][0], yoko_block[light[i][0]][x-1]+1, yoko_block[light[i][0]][x]-1))
    y = bisect.bisect(tate_block[light[i][1]], light[i][0])
    tate_set.add((light[i][1], tate_block[light[i][1]][y-1]+1, tate_block[light[i][1]][y]-1))

yoko = [[] for _ in range(H)]
tate = [[] for _ in range(W)]
for i, l, r in yoko_set:
    bisect.insort(yoko[i], l)
    bisect.insort(yoko[i], r)
for j, l, r in tate_set:
    bisect.insort(tate[j], l)
    bisect.insort(tate[j], r)

ans = 0
for i in range(H):
    for j in range(0, len(yoko[i]), 2):
        ans += yoko[i][j+1] - yoko[i][j] + 1
        for k in range(yoko[i][j], yoko[i][j+1]+1):
            if len(tate[k])==0: continue
            z = bisect.bisect_left(tate[k], i)
            if z==len(tate[k]): continue
            if tate[k][z]==i or z%2:
                ans -= 1
for j in range(W):
    for i in range(0, len(tate[j]), 2):
        ans += tate[j][i+1] - tate[j][i] + 1

print(ans)
