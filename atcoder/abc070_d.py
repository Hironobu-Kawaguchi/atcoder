# https://atcoder.jp/contests/abc070/tasks/abc070_d

import sys
sys.setrecursionlimit(10**6)
INF = 1001001001

N = int(input())
g = [[] for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    g[a-1].append([b-1, c])
    g[b-1].append([a-1, c])
Q, K = map(int, input().split())
dist = [INF] * N
dist[K-1] = 0

def dfs(n, d):
    if dist[n] == INF:
        dist[n] = d
    for i, c in g[n]:
        if dist[i] == INF:
            dfs(i, dist[n]+c)
    return

dfs(K-1, 0)
# print(dist)

for i in range(Q):
    x, y = map(int, input().split())
    print(dist[x-1]+dist[y-1])
