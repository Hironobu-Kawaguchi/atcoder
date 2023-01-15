# https://atcoder.jp/contests/typical90/tasks/typical90_bu
# 木DP
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

N = int(input())
c = list(input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
dp = [[0]*3 for _ in range(N)]
visited = [False] * N

def dfs(pos, pre):
    if visited[pos]:
        return
    visited[pos] = True
    cnt_a = 1
    cnt_b = 1
    cnt_ab = 1
    for v in G[pos]:
        if v==pre: continue
        dfs(v, pos)
        if c[pos]=='a':
            cnt_a *= dp[v][0] + dp[v][2]
            cnt_a %= MOD
        else:
            cnt_b *= dp[v][1] + dp[v][2]
            cnt_b %= MOD
        cnt_ab *= dp[v][0] + dp[v][1] + 2 * dp[v][2]
        cnt_ab %= MOD
    if c[pos]=='a':
        dp[pos][0] = cnt_a % MOD
        dp[pos][2] = (cnt_ab - cnt_a + MOD) % MOD
    else:
        dp[pos][1] = cnt_b % MOD
        dp[pos][2] = (cnt_ab - cnt_b + MOD) % MOD
    return

dfs(0, -1)
print(dp[0][2])
# print(dp)
