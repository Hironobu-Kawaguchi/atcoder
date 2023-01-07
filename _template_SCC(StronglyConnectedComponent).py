# https://atcoder.jp/contests/typical90/tasks/typical90_u
# 強連結成分分解 SCC: Strongly Connected Component

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


N, M = map(int, input().split())

used = [False] * N
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]
I = []
cnts = 0

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    H[b-1].append(a-1)

def dfs(pos):
    used[pos] = True
    for i in G[pos]:
        if used[i] is False: dfs(i)
    I.append(pos)
    return

def dfs2(pos):
    global cnts
    used[pos] = True
    cnts += 1
    for i in H[pos]:
        if used[i] is False: dfs2(i)
    return

for i in range(N):
    if used[i] is False: dfs(i)

ans = 0
I.reverse()
used = [False] * N
for i in I:
    if used[i]: continue
    cnts = 0
    dfs2(i)
    ans += cnts * (cnts - 1) // 2

print(ans)
