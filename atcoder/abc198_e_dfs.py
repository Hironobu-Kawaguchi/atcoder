# https://atcoder.jp/contests/abc198/tasks/abc198_e

import sys
sys.setrecursionlimit(1000000)

N = int(input())
C = list(map(int, (input().split())))
G = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
# print(G)

Cs = [False] * (10**5+5)
Visited = [False]*N
Good = [False]*N
Good[0] = True

def dfs(now, Cs, Good):
    if Visited[now]: return
    Visited[now] = True
    for next in G[now]:
        if Visited[next]: continue
        # print(next, C[next], Cs[now])
        if Cs[C[next]] == 0:
            Good[next] = True
        Cs[C[next]] += 1
        dfs(next, Cs, Good)
        Cs[C[next]] -= 1
    return

Cs[C[0]] += 1
dfs(0, Cs, Good)
# print(Cs)
# print(Visited)
# print(Good)

for i in range(N):
    if Good[i]:
        print(i+1)

