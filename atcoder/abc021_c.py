# https://atcoder.jp/contests/abc021/tasks/abc021_c

from collections import deque
MOD = 10**9+7

N = int(input())
a, b = map(int, input().split())
M = int(input())
to = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    to[x-1].append(y-1)
    to[y-1].append(x-1)

dp = [-1] * N
dp[a-1] = 0
Cnt = [0] * N
Cnt[a-1] = 1

q = deque()
q.append(a-1)
while q:
    v = q.popleft()
    for i in to[v]:
        if dp[i] == -1:
            dp[i] = dp[v] + 1
            Cnt[i] += Cnt[v]
            q.append(i)
        elif dp[i] == dp[v] + 1:
            Cnt[i] += Cnt[v]

print(Cnt[b-1]%MOD)
