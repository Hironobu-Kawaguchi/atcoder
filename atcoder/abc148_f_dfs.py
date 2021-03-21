# https://atcoder.jp/contests/abc148/tasks/abc148_f

import sys
sys.setrecursionlimit(1000000)

N, s, t = map(int, input().split())
s -= 1
t -= 1
to = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

def dfs(dist, v, d=0, p=-1):
    dist[v] = d
    for u in to[v]:
        if u == p:
            continue
        dfs(dist, u, d+1, v)

def calcDist(s):
    dist = [0] * N
    dfs(dist, s)
    return dist

distS = calcDist(s)
distT = calcDist(t)

mx = 0
for i in range(N):
    if distS[i] < distT[i]:
        mx = max(mx, distT[i])
ans = mx - 1
print(ans)
