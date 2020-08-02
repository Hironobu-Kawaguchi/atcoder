# https://atcoder.jp/contests/abc106/tasks/abc106_d

import sys
input = sys.stdin.buffer.readline

N, M, Q = map(int, input().split())
L, R = [], []
X = [[0]*N for _ in range(N)]
for i in range(M):
    l, r = map(int, input().split())
    L.append(l-1)
    R.append(r-1)
    X[l-1][r-1] += 1
C =[[0]*(N+1) for _ in range(N)]
for i in range(N):
    for j in range(N):
        C[i][j+1] = C[i][j] + X[i][j]

for i in range(Q):
    p, q = map(int, input().split())
    ans = 0
    for j in range(p-1, q):
        ans += C[j][q] - C[j][p-1]
    print(ans)
