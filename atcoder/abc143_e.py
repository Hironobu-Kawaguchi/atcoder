# https://atcoder.jp/contests/abc143/tasks/abc143_e

INF = 1001001001
N, M, L = map(int, input().split())

fuel = [[INF] * N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    fuel[A][B] = C
    fuel[B][A] = C
for i in range(N):
    fuel[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            fuel[i][j] = min(fuel[i][j], fuel[i][k] + fuel[k][j])

dist = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        elif fuel[i][j] <= L:
            dist[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

Q = int(input())
for i in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if dist[s][t] == INF:
        print(-1)
    else:
        print(dist[s][t] - 1)
