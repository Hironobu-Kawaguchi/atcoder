# https://atcoder.jp/contests/abc075/tasks/abc075_c

def dfs(v, N, graph, visited):
    visited[v] = True
    for v2 in range(N):
        if graph[v][v2] == False:
            continue
        if visited[v2] == True:
            continue
        dfs(v2, N, graph, visited)

N, M = map(int, input().split())
a, b = [], []
graph = [[False] * N for _ in range(N)]
for i in range(M):
    _a, _b = map(int, input().split())
    a.append(_a - 1), b.append(_b - 1)
    graph[a[i]][b[i]] = graph[b[i]][a[i]] = True

ans = 0

for i in range(M):
    graph[a[i]][b[i]] = graph[b[i]][a[i]] = False
    visited = [False] * N
    dfs(0, N, graph, visited)
    bridge = False
    for j in range(N):
        if visited[j] == False:
            bridge = True
    if bridge:
        ans += 1
    graph[a[i]][b[i]] = graph[b[i]][a[i]] = True

print(ans)
