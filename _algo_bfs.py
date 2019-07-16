# C - 幅優先探索 (BFS: breadth first search)
# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
cs = []
for r in range(R):
    cs.append(input())

vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]
q = deque([(sy, sx, 0)])
s = set()
s.add((sy, sx))
goal = False

while goal == False:
    y, x, n = q.popleft()
    for i in range(4):
        ny = y + vy[i]
        nx = x + vx[i]
        if [gy, gx] == [ny, nx]:
            print(n+1)
            goal = True
            break
        elif cs[ny-1][nx-1] == '.' and ((ny, nx) not in s):
            s.add((ny, nx))
            q.append((ny, nx, n+1))
