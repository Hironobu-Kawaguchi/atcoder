# https://atcoder.jp/contests/abc179/tasks/abc179_d

MOD = 998244353
n, k = map(int, input().split())
l, r = [0]*k, [0]*k
for i in range(k):
    _l, _r = map(int, input().split())
    l[i], r[i] = _l, _r
dp, dpsum = [0]*(n+1), [0]*(n+1)
dp[1], dpsum[1] = 1, 1
for i in range(2, n+1):
    for j in range(k):
        li = i - r[j]
        ri = i - l[j]
        if ri<0: continue
        li = max(li, 1)
        dp[i] += dpsum[ri] - dpsum[li-1]
        dp[i] %= MOD
    dpsum[i] = dpsum[i-1] + dp[i]
print(dp[n])
