# https://atcoder.jp/contests/arc048/tasks/arc048_b

N = int(input())

cnt = [[0]*4 for _ in range(100005)]
R, H = [], []
for i in range(N):
    r, h = map(int, input().split())
    R.append(r)
    H.append(h)
    cnt[r][h-1] += 1
    cnt[r][3] += 1
csum = [[0]*4 for _ in range(100005)]
for i in range(100000):
    for j in range(4):
        csum[i+1][j] = csum[i][j] + cnt[i+1][j]

for i in range(N):
    win = csum[R[i]-1][3] + cnt[R[i]][H[i]%3]
    lose = N - csum[R[i]][3] + cnt[R[i]][(H[i]+1)%3]
    draw = cnt[R[i]][H[i]-1] - 1    # 自分を除外
    print(win, lose, draw)
