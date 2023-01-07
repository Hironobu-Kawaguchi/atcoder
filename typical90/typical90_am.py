# https://atcoder.jp/contests/typical90/tasks/typical90_am

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
to = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)

dp = [0] * N

def dfs(pos, pre):
    dp[pos] = 1
    for i in to[pos]:
        if i==pre: continue
        dfs(i, pos)
        dp[pos] += dp[i]

dfs(0, -1)

ans = 0
for i in range(N):
    ans += dp[i] * (N - dp[i])

print(ans)
