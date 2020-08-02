# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b

MOD = 998244353
import collections
N = int(input())
D = list(map(int, input().split()))
mx = max(D)
c = collections.Counter(D)

if D[0] == 0 and c[0] == 1:
    ans = 1
    for i in range(1, mx+1):
        if i not in c:
            ans = 0
            break
        else:
            ans *= (c[i-1] ** c[i]) % MOD
            ans %= MOD
else:
    ans = 0

print(ans)
