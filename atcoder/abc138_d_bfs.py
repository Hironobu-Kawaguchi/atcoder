# https://atcoder.jp/contests/abc138/tasks/abc138_d

from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
# print(G)

DP = [0] * N
for j in range(Q):
    p, x = map(int, input().split())
    DP[p-1] += x

# BFS
que = deque([])
que.append((0, DP[0]))
while que:
    p = que.popleft()
    v = p[1]
    for i in G[p[0]]:
        DP[i] += v
        que.append((i, DP[i]))

print(*DP)
