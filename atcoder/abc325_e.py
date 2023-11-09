# https://atcoder.jp/contests/abc325/tasks/abc325_e

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

import heapq
INF = 1e18

N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

G = [[[[] for _ in range(N)] for _ in range(N)] for _ in range(2)]
for i in range(N):
    for j in range(N):
        G[1][i][j] = D[i][j] * A        # car
        G[0][i][j] = D[i][j] * B + C    # train

# dijkstra
dist = [[INF] * N for _ in range(2)]
dist[0][0] = 0
dist[1][0] = 0
q = [(0, 0, 0), (0, 0, 1)]  # (dist, v, is_car)
while q:
    d, v, is_car = heapq.heappop(q)
    if dist[is_car][v] < d:
        continue
    for nv in range(N):
        if v==nv: continue
        # trainはどちらからもOK
        nd = d + G[0][v][nv]
        if dist[0][nv] > nd:
            dist[0][nv] = nd
            heapq.heappush(q, (nd, nv, 0))
        if is_car:    # carからはcarがOK
            nd = d + G[1][v][nv]
            if dist[1][nv] > nd:
                dist[1][nv] = nd
                heapq.heappush(q, (nd, nv, 1))
# for i in range(N):
#     print("dist", i, dist[0][i], dist[1][i])
ans = min(dist[0][N-1], dist[1][N-1])
print(ans)
