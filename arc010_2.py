# https://atcoder.jp/contests/arc010/tasks/arc010_2

ds = [0,31,29,31,30,31,30,31,31,30,31,30,31]
s = [[0]*32 for _ in range(13)]
x = 0
for m in range(1, 12+1):
    for d in range(1, ds[m]+1):
        if (x%7==0 or x%7==6):
            s[m][d] = 1
        x += 1

N = int(input())
for i in range(N):
    m, d = map(int, input().split('/'))
    s[m][d] += 1

x, y, ans = 0, 0, 0
for m in range(1, 12+1):
    for d in range(1, ds[m]+1):
        x += s[m][d]
        if x:
            x -= 1
            y += 1
        else:
            y = 0
        ans = max(ans, y)

print(ans)
