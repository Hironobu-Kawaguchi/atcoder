# https://atcoder.jp/contests/abc018/tasks/abc018_3

R, C, K = map(int, input().split())
s = []
for _ in range(R):
    s.append(input())
up    = [[0] * C for _ in range(R)]
down  = [[0] * C for _ in range(R)]

for j in range(C):
    cnt = 0
    for i in range(R):
        if s[i][j] == 'o':
            cnt += 1
        else:
            cnt = 0
        up[i][j] = cnt

for j in range(C):
    cnt = 0
    for i in range(R-1, -1, -1):
        if s[i][j] == 'o':
            cnt += 1
        else:
            cnt = 0
        down[i][j] = cnt

ans = 0
for x in range(K-1, R-K+1):
    for y in range(K-1, C-K+1):
        flg = True
        for z in range(-K+1, K):
            j = y+z
            chk = K-abs(z)
            if up[x][j] < chk or down[x][j] < chk:
                flg = False
                break
        if flg:
            ans += 1
            # print(x, y)
print(ans)
