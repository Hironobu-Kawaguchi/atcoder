# https://atcoder.jp/contests/abc277/tasks/abc277_e

import sys
input = sys.stdin.buffer.readline
from collections import deque
INF = 1001001001

N, M, K = map(int, input().split())
N2 = N*2
G = [[] for _ in range(N2)]
for i in range(M):
    u, v, a = map(int, input().split())
    u -= 1; v -= 1
    if a==1:
        G[u].append((v,1))
        G[v].append((u,1))
    else:
        G[u+N].append((v+N,1))
        G[v+N].append((u+N,1))
s = list(map(int, input().split()))
for i in range(K):
    v = s[i] - 1
    G[v].append((v+N,0))
    G[v+N].append((v,0))
# print(G)

dist = [INF] * N2
dist[0] = 0
que = deque()
que.append((0,0))
while que:
    d, u = que.popleft()
    if dist[u]!=d: continue
    for v, cost in G[u]:
        nd = d + cost
        if nd >= dist[v]: continue
        dist[v] = nd
        if cost:
            que.append((nd, v))
        else:
            que.appendleft((nd, v))
# print(dist)

ans = min(dist[N-1], dist[N2-1])
if ans==INF:
    ans = -1
print(ans)
