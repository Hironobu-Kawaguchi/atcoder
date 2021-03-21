# https://atcoder.jp/contests/abc080/tasks/abc080_c

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -(1<<30)
for b in range(1, (1<<10)):
    tmp = 0
    for i in range(N):
        cnt = 0
        for j in range(10):
            if (b>>j&1) and F[i][j]:
                cnt += 1
        tmp += P[i][cnt]
    ans = max(ans, tmp)

print(ans)
