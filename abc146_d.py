# https://atcoder.jp/contests/abc146/tasks/abc146_d

import sys
sys.setrecursionlimit(10**8)

N = int(input())
g = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, i))
    g[b].append((a, i))

ans = [0] * (N-1)

def dfs(v, c=-1, p=-1):
    global g, ans
    k = 1
    for u, ei in g[v]:
        if u == p:
            continue
        if k == c:
            k += 1
        ans[ei] = k
        k += 1
        dfs(u, ans[ei], v)

dfs(0)
mx = 0
for i in range(N):
    mx = max(mx, len(g[i]))
print(mx)
for i in range(N-1):
    print(ans[i])
