# https://atcoder.jp/contests/toyota2023summer-final/tasks/toyota2023summer_final_a
# from numba import njit

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque
import heapq

D, N = map(int, input().split())
cn = D*D - 1 - N
# print(cn, file=sys.stderr)
sy, sx = (0, (D-1)//2)
WholeSales = [[-1]*D for _ in range(D)]
WholeSales[sy][sx] = -2
r_pos = []
for _ in range(N):
    y, x = map(int, input().split())
    WholeSales[y][x] = -2
containers = [[] for _ in range(cn)]

no_wall = [[False]*D for _ in range(D)]
for y in range(D):
    for x in range(D):
        flg = True
        for dy in [-1, 0, 1]:
            ny = y + dy
            for dx in [-1, 0, 1]:
                nx = x + dx
                if ny == sy and nx == sx: continue
                if 0 > ny or ny >= D or 0 > nx or nx >= D:
                    flg = False
                    break
                if WholeSales[ny][nx] == -2:
                    flg = False
                    break
        if flg: no_wall[y][x] = True
# print(no_wall, file=sys.stderr)
    
dist = [[-1]*D for _ in range(D)]
dist[sy][sx] = 0
q = deque([(sy, sx, 0)])
while q:
    y, x, d = q.popleft()
    dist[y][x] = d
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < D and 0 <= nx < D and dist[ny][nx]==-1 and WholeSales[ny][nx] == -1:
            q.append((ny, nx, d+1))
# print(dist, file=sys.stderr)

# able_pos = []
# for y in range(D):
#     for x in range(D):
#         if dist[y][x] > 0:
#             able_pos.append((dist[y][x], y, x))
# able_pos.sort(reverse=True)   ### 遠い順における場所

no_wall_pos_tmp = []
for y in range(D):
    for x in range(D):
        if no_wall[y][x]:
            no_wall_pos_tmp.append((dist[y][x], y, x))
no_wall_pos_tmp.sort()   ### 周囲に壁がないところは，コンテナ番号が小さいコンテナ用の場所
no_wall_pos = []
no_wall_put = [[False]*D for _ in range(D)]
no_wall_pos.append(no_wall_pos_tmp[0])
no_wall_put[no_wall_pos_tmp[0][1]][no_wall_pos_tmp[0][2]] = True
for i in range(1, len(no_wall_pos_tmp)):
    d, y, x = no_wall_pos_tmp[i]
    flg = True
    for dy in [-1, 0, 1]:
    # for dy in [-2, -1, 0, 1, 2]:
        ny = y + dy
        for dx in [-1, 0, 1]:
        # for dx in [-2, -1, 0, 1, 2]:
            nx = x + dx
            if 0 > ny or ny >= D or 0 > nx or nx >= D: continue
            if no_wall_put[ny][nx]:
                flg = False
                break
        if not flg: break
    # for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #     ny = y + dy
    #     nx = x + dx
    #     if 0 > ny or ny >= D or 0 > nx or nx >= D: continue
    #     if no_wall_put[ny][nx]:
    #         flg = False
    #         break
    if flg:
        no_wall_pos.append((d, y, x))
        no_wall_put[y][x] = True
# print(no_wall_put, file=sys.stderr)
# print(len(no_wall_pos), no_wall_pos, file=sys.stderr)

    
dist_able = [[-1]*D for _ in range(D)]
dist_able[sy][sx] = 0
q = deque([(sy, sx, 0)])
while q:
    y, x, d = q.popleft()
    dist_able[y][x] = d
    if not (y == sy and x == sx) and no_wall_put[y][x]: continue   # 予約したところは使えなくなる
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < D and 0 <= nx < D and dist_able[ny][nx]==-1 and WholeSales[ny][nx] == -1:
            q.append((ny, nx, d+1))
# print(dist_able, file=sys.stderr)

able_pos = []
for y in range(D):
    for x in range(D):
        if dist[y][x] > 0:
            able_pos.append((dist_able[y][x], y, x))
able_pos.sort(reverse=True)   ### 遠い順における場所



# @njit
def main():
    put_pos = []
    now = 0
    for i in range(cn):
        ci = int(input())
        if ci < len(no_wall_pos) and WholeSales[no_wall_pos[ci][1]][no_wall_pos[ci][2]] == -1:
            d, y, x = no_wall_pos[ci]
        else:
            for j in range(now, len(able_pos)):
                d, y, x = able_pos[j]
                if WholeSales[y][x] == -1:
                    now = j + 1
                    break
        print(y, x, flush=True)
        put_pos.append((d, ci, y, x))
        containers[ci] = [y, x]
        WholeSales[y][x] = ci
    # print(containers, file=sys.stderr)
    put_pos.sort()

    ans = []
    q = []
    putted = [False] * cn
    heapq.heappush(q, (-1, sy, sx))
    while q:
        ci, y, x = heapq.heappop(q)
        if ci>=0:
            ans.append([y, x])
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < D and 0 <= nx < D and WholeSales[ny][nx] >= 0 and not putted[WholeSales[ny][nx]]:
                heapq.heappush(q, (WholeSales[ny][nx], ny, nx))
                putted[WholeSales[ny][nx]] = True
    
    # for i in range(cn):
    #     ans.append([put_pos[i][2], put_pos[i][3]])
    for y, x in ans:
        print(y, x)

    B = 0
    for i in range(cn):
        bi = WholeSales[ans[i][0]][ans[i][1]]
        for j in range(i+1, cn):
            bj = WholeSales[ans[j][0]][ans[j][1]]
            if bi > bj:
                B += 1
    score = 10**9 * ((D*D - N)*(cn)/2 - B) / ((D*D - N)*(cn)/2)
    print(F"Score: {score:,.0f}", file=sys.stderr)
    return

main()
