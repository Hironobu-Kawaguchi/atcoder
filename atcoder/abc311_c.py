# https://atcoder.jp/contests/abc310/tasks/abc310_c
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, (input().split())))
G = [[] for _ in range(N)]
for i in range(N):
    G[i].append(A[i]-1)
# print(G, file=sys.stderr)

# BFS
from collections import deque
oks = []
for i in range(N):
    d = [-1]*N
    # if d[i]!=-1: continue
    q = deque()
    q.append(i)
    d[i] = 0
    flg = False
    visited = [False]*N
    visited[i] = True
    while q:
        v = q.popleft()
        for nv in G[v]:
            if visited[nv]:
                flg = True
                oks.append(nv)
                break
            if visited[nv]:
                continue
            d[nv] = d[v] + 1
            visited[nv] = True
            q.append(nv)
        if flg:
            break
    if len(oks)>=1:
        break
# print(d, file=sys.stderr)
# print(oks, file=sys.stderr)

ans = [oks[0]+1]
q = deque()
q.append(oks[0])
flg = False
while q:
    v = q.popleft()
    for nv in G[v]:
        if d[v]>d[ans[0]-1] + 1 and nv==ans[0]-1:
            # ans.append(nv+1)
            flg = True
            break
        if d[nv]==d[v]+1:
            q.append(nv)
            ans.append(nv+1)
        break
    if flg:
        break

print(len(ans))
print(*ans)
