# https://atcoder.jp/contests/abc126/tasks/abc126_e

import sys
sys.setrecursionlimit(10**6)

def dfs(x, g, vis):
    if vis[x]:
        return
    vis[x] = 1
    for y in g[x]:
        dfs(y, g, vis)

def main():
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]
    for i in range(M):
        X, Y, Z = map(int, input().split())
        X -= 1
        Y -= 1
        g[X].append(Y)
        g[Y].append(X)
    vis = [0] * N

    ans = 0
    for i in range(N):
        if vis[i] == 0:
            dfs(i, g, vis)
            ans += 1
    print(ans)

main()