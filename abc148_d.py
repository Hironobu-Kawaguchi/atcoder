# https://atcoder.jp/contests/abc148/tasks/abc148_d

N = int(input())
a = list(map(int, input().split()))
ans = N
now = 1
for i in range(N):
    if a[i] == now:
        ans -= 1
        now += 1

if ans == N:
    print(-1)
else:
    print(ans)
