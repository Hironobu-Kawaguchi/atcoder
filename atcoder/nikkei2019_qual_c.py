# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c

n = int(input())
dif = []
sumb = 0
for i in range(n):
    a, b = map(int, input().split())
    sumb += b
    dif.append(a+b)
dif.sort(reverse=True)
ans = -sumb
for i in range(n):
    if i%2 == 0:
        ans += dif[i]
print(ans)
