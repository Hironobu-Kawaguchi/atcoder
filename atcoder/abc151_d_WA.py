# https://atcoder.jp/contests/abc151/tasks/abc151_d

H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)
INF = 10**9

V = H*W
d = [[INF for _ in range(V)] for _ in range(V)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            v = i*H + j
            d[v][v] = 0
            if i != 0 and S[i-1][j] == '.':
                x = (i-1)*H + j
                d[v][x] = 1
                d[x][v] = 1
            if i != H-1 and S[i+1][j] == '.':
                x = (i+1)*H + j
                d[v][x] = 1
                d[x][v] = 1
            if j != 0 and S[i][j-1] == '.':
                x = i*H + j-1
                d[v][x] = 1
                d[x][v] = 1
            if j != W-1 and S[i][j+1] == '.':
                x = i*H + j+1
                d[v][x] = 1
                d[x][v] = 1

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

d = warshall_floyd(d)
# print(d)
ans = 0
for i in range(V):
    for j in range(V):
        if d[i][j] != INF:
            ans = max(ans, d[i][j])

print(ans)
