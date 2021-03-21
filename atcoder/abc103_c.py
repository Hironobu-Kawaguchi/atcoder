# https://atcoder.jp/contests/abc103/tasks/abc103_c

import fractions

N = int(input())
a = list(map(int, input().split()))

m = 1
for i in range(N):
    m = (a[i] * m) // fractions.gcd(a[i], m)    # 最小公倍数を計算
m -= 1    # m = 最小公倍数 - 1

ans = 0
for i in range(N):
    ans += m % a[i]

print(ans)
