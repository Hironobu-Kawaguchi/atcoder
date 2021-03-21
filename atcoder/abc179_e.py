# https://atcoder.jp/contests/abc179/tasks/abc179_e

n, x, m = map(int, input().split())
idx = [-1] * m
a = []
leng = 0
tot = 0

while idx[x] == -1:
    a.append(x)
    idx[x] = leng
    leng += 1
    tot += x
    x = (x*x)%m

c = leng - idx[x]
s = 0
for i in range(idx[x], leng):
    s += a[i]

ans = 0
if n<=leng:
    for i in range(n):
        ans += a[i]
else:
    ans += tot
    n -= leng
    ans += s*(n//c)
    n %= c
    for i in range(n):
        ans += a[idx[x]+i]

print(ans)
