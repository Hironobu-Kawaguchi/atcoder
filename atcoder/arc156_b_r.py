# https://atcoder.jp/contests/arc156/tasks/arc156_b
# https://atcoder.jp/contests/arc156/editorial/5718

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

MAXN = 5 * 10 ** 5
fact = [1]
ifact = [1]
for i in range(MAXN):
    fact.append(fact[-1] * (i+1) % MOD)
    ifact.append(pow(fact[-1], MOD-2, MOD))
def nCr(n, r):
    return fact[n] * ifact[r] * ifact[n-r] % MOD

N, K = map(int, input().split())
A = list(map(int, (input().split())))

used = [False] * (5 * 10 ** 5)
for i in range(N):
    used[A[i]] = True

ans = 0
cnt = 0
for x in range(N + K):
    if cnt>=K: break
    ans += nCr(x+K-1-cnt, x)
    ans %= MOD
    # print(x, ans)
    if used[x]==False:
        cnt += 1

print(ans)
