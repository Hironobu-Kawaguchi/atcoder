# https://atcoder.jp/contests/abc142/tasks/abc142_e

INF = 1001001001

N, M = map(int, input().split())
key = []
for i in range(M):
    a, b = map(int, input().split())
    s = 0
    c = list(map(int, input().split()))
    for j in range(b):
        c[j] -= 1
        s |= 1<<c[j]
    key.append([s, a])
dp = [INF] * (1<<N)
dp[0] = 0
for s in range(1<<N):
    for i in range(M):
        t = s | key[i][0]
        cost = dp[s] + key[i][1]
        dp[t] = min(dp[t], cost)
ans = dp[-1]
if ans == INF:
    ans = -1
print(ans)
