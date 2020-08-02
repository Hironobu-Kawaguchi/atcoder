# https://atcoder.jp/contests/abc132/tasks/abc132_e
# https://atcoder.jp/contests/abc132/submissions/6188357
from collections import deque
N, M = map(int, input().split())
INF = 1001001001
dist = [[INF for _ in range(3)] for _ in range(N)]

# 有向グラフG
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)

S, T = map(int, input().split())
S -= 1
T -= 1

# BFS
q = deque()
q.append((S, 0))
dist[S][0] = 0

while q:
    k, l = q.popleft()
    for i in G[k]:
        nl = (l + 1) % 3
        if dist[i][nl] == INF:
            dist[i][nl] = dist[k][l] + 1
            q.append((i, nl))

ans = dist[T][0]
if ans == INF:
    ans = -1
else:
    ans //= 3
print(ans)
