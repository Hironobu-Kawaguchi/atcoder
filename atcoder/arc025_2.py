# https://atcoder.jp/contests/arc025/tasks/arc025_2

from itertools import combinations
H,W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(H)]

cum = [[0]*(W+1) for i in range(H+1)]
for i in range(H):
    for j in range(W):
        if (i+j)%2:
            cum[i+1][j+1] = cum[i+1][j] + cum[i][j+1] -cum[i][j] + C[i][j]
        else:
            cum[i+1][j+1] = cum[i+1][j] + cum[i][j+1] -cum[i][j] - C[i][j]
# print(cum)
ans = 0
for i1, i2 in combinations(range(H+1), 2):
    for j1, j2 in combinations(range(W+1), 2):
        if cum[i2][j2] + cum[i1][j1] == cum[i2][j1] + cum[i1][j2]:
            ans = max(ans, (i2-i1)*(j2-j1))
print(ans)
