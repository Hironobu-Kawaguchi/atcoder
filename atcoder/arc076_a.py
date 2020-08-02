# https://atcoder.jp/contests/abc065/tasks/arc076_a

MOD = 1000000007
N, M = map(int, input().split())

def p(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        res %= MOD
    return res

if abs(N-M) == 0:
    tmp = p(N)
    ans = tmp * tmp * 2 % MOD
elif abs(N-M) == 1:
    tmp = p(min(N,M))
    ans = tmp * tmp *max(N,M) % MOD
else:
    ans = 0

print(ans)
