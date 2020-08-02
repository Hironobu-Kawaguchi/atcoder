# https://atcoder.jp/contests/abc012/tasks/abc012_4
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

INF = 1001001001
N, M = map(int, input().split())
g = [[INF]*N for _ in range(N)]
for i in range(N):
    g[i][i] = 0
for i in range(M):
    a, b, t = map(int, input().split())
    g[a-1][b-1] = t
    g[b-1][a-1] = t

for k in range(N):
    for i in range(N):
        for j in range(N):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])
ans = INF
for i in range(N):
    ans = min(ans, max(g[i]))
print(ans)
