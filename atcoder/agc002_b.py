# https://atcoder.jp/contests/agc002/tasks/agc002_b

n, m = map(int, input().split())
num = [1] * n
red = [0] * n
red[0] = 1

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if red[x]:
        red[y] = 1
    num[x] -= 1
    num[y] += 1
    if num[x] == 0:
        red[x] = 0

ans = 0
for i in range(n):
    if red[i]:
        ans += 1
print(ans)
