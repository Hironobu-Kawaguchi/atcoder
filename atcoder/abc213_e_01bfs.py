# https://atcoder.jp/contests/ABC213/tasks/abc213_e

# import heapq
from collections import deque
dy = [-1, 1, 0, 0]
dx = [ 0, 0, 1,-1]
py = [-2,-2,-2,-1,-1,-1,-1,-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
px = [-1, 0, 1,-2,-1, 0, 1, 2,-2,-1, 1, 2,-2,-1, 0, 1, 2,-1, 0, 1]
INF = 1001001001

H, W = map(int, input().split())
map = []
dist = [[INF]*W for _ in range(H)]
for i in range(H):
    S = input().rstrip()
    map.append(S)
# h = []
# heapq.heappush(h, (0, 0, 0))
q = deque([(0,0,0)])
ans = 0
while len(q):
    # d, y, x = heapq.heappop(h)
    d, y, x = q.pop()
    if y==H-1 and x==W-1:
        ans = d
        break
    for i in range(4):
        ny = y + dy[i]
        if ny<0 or ny>=H: continue
        nx = x + dx[i]
        if nx<0 or nx>=W: continue
        if map[ny][nx]=='#': continue
        if d < dist[ny][nx]:
            # heapq.heappush(h, (d, ny, nx))
            q.append((d, ny, nx))
            dist[ny][nx] = d
    for i in range(20):
        ny = y + py[i]
        if ny<0 or ny>=H: continue
        nx = x + px[i]
        if nx<0 or nx>=W: continue
        nd = d + 1
        if nd < dist[ny][nx]:
            # heapq.heappush(h, (d+1, ny, nx))
            q.appendleft((nd, ny, nx))
            dist[ny][nx] = nd
print(ans)
