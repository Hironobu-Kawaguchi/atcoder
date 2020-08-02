# A - Candy Distribution Again
# https://atcoder.jp/contests/agc027/tasks/agc027_a
N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(N):
    if a[i] <= x:
        x -= a[i]
        ans += 1
    else:
        break
if x == 0 or ans != N:
    print(ans)
else:
    print(max(ans - 1, 0))
