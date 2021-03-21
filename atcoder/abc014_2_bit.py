# https://atcoder.jp/contests/abc014/tasks/abc014_2

n, X = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if X>>i&1:
        ans += a[i]
print(ans)
