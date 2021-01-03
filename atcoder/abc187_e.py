# https://atcoder.jp/contests/abc187/tasks/abc187_e

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)

n = int(input())
es = [[] for _ in range(n)]
depth = [-1]*n
imos = [0]*n

def depthDFS(depth, u, d):
    """ 深さを求めるDFS """
    depth[u] = d
    for v in es[u]:
        if depth[v]==-1:
            depthDFS(depth, v, d+1)

def imosDFS(imos, u, c):
    """ 差分から実際の値に変換するDFS """
    c += imos[u]
    imos[u] = c
    for v in es[u]:
        if depth[v] > depth[u]:
            imosDFS(imos, v, c)

a, b = [], []
for i in range(n-1):
    _a, _b = map(int, input().split())
    a.append(_a-1)
    b.append(_b-1)
    es[a[i]].append(b[i])
    es[b[i]].append(a[i])
depthDFS(depth,0,0)
q = int(input())
for qi in range(q):
    t, e, x = map(int, input().split())
    e -= 1
    if t==1:
        va = a[e]
        vb = b[e]
    else:
        va = b[e]
        vb = a[e]
    if depth[va] < depth[vb]:   # aの方が根側
        imos[0] += x  # 根に足す
        imos[vb] -= x  # 通らない部分木を引く
    else:
        imos[va] += x  # 部分木に足す

imosDFS(imos,0,0)

for i in range(n):
    print(imos[i])
