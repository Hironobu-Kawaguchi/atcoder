# https://atcoder.jp/contests/abc016/tasks/abc016_3

N, M = map(int, input().split())
g = [[0] * N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a-1][b-1] = 1
    g[b-1][a-1] = 1

for i in range(N):
    f = set()
    ff = set()
    for j in range(N):
        if g[i][j] == 1:
            f.add(j)
    for k in f:
        for j in range(N):
            if i != j and g[k][j] == 1:
                ff.add(j)
    print(len(ff-f))
