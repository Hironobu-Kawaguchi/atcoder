# https://atcoder.jp/contests/abc079/tasks/abc079_d

h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            if c[i][j] > c[i][k] + c[k][j]:
                c[i][j] = c[i][k] + c[k][j]
ans = 0
for i in range(h):
    a = list(map(int, input().split()))
    for j in range(w):
        if a[j] >= 0:
            ans += c[a[j]][1]
print(ans)
