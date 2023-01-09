# https://atcoder.jp/contests/ABC284/tasks/abc284_e

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
MAX = 10**6

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
K = 0
# K = 999990

visited = [False] * N

def dfs(pos):
    global K
    if K==MAX:
        return
    K += 1
    visited[pos] = True
    for i in G[pos]:
        if visited[i]: continue
        dfs(i)
    visited[pos] = False
    return

dfs(0)
print(K)
