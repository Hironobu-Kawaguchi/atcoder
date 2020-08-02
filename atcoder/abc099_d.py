# https://atcoder.jp/contests/abc099/tasks/abc099_d

from itertools import permutations

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

t = [[0]*C for _ in range(3)]
for i in range(N):
    for j in range(N):
        t[(i+j)%3][c[i][j]-1] += 1

ans = 1001001001
for i, j, k in permutations(range(C), 3):
    tmp = 0
    for l in range(C):
        tmp += D[l][i] * t[0][l]
    for l in range(C):
        tmp += D[l][j] * t[1][l]
    for l in range(C):
        tmp += D[l][k] * t[2][l]
    ans = min(ans, tmp)
print(ans)
