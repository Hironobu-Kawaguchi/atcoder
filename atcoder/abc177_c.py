# https://atcoder.jp/contests/abc177/tasks/abc177_c

MOD = 10**9+7
n = int(input())
a = list(map(int, input().split()))

ans = sum(a)**2
for i in range(n):
    ans -= a[i]*a[i]
ans //= 2
ans %= MOD
print(ans)
