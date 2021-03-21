# https://atcoder.jp/contests/abc022/tasks/abc022_c

from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall

N, M = map(int, input().split())

INF = float('inf')
G = [[INF] * N for _ in range(N)]
from_0 = []
for i in range(M):
    u, v, l = map(int, input().split())
    if u == 1:
        from_0.append((v-1, l))
    else:
        G[u-1][v-1] = l
G = floyd_warshall(G, 0)
ans = INF

for x, y in permutations(from_0, 2):
    ans = min(ans, x[1] + y[1] + G[x[0]][y[0]])
print(-1 if ans == INF else int(ans))
