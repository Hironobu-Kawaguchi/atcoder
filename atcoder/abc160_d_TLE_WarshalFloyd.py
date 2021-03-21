# https://atcoder.jp/contests/abc160/tasks/abc160_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

INF = 1001001001
N, X, Y = map(int, input().split())
d = [[INF]*N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for i in range(N-1):
    d[i][i+1] = 1
    d[i+1][i] = 1
d[X-1][Y-1] = 1
d[Y-1][X-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ans = [0]*(N-1)
for i in range(N-1):
    for j in range(i+1,N):
        ans[d[i][j]-1] += 1
for i in range(N-1):
    print(ans[i])
