# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_c

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = -a[0] + a[n-1]
for i in range(1, n-1):
    ans += abs(a[i])
print(ans)
x = a[0]
y = a[n-1]
for i in range(1, n-1):
    if a[i] > 0:
        print(x, a[i])
        x -= a[i]
    else:
        print(y, a[i])
        y -= a[i]
print(y, x)
