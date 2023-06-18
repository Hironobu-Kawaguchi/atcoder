# 強連結成分分解 SCC: Strongly Connected Component
# https://atcoder.jp/contests/abc296/tasks/abc296_e

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, result):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, result)
        result.append(v)

    def dfs_transpose(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_transpose(i, visited, component)

    def transpose(self):
        gt = Graph(self.V)
        for i in range(self.V):
            for j in self.graph[i]:
                gt.add_edge(j, i)
        return gt

    def find_scc(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        gt = self.transpose()
        visited = [False] * self.V
        scc = []

        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gt.dfs_transpose(i, visited, component)
                scc.append(component)

        return scc

N = int(input())
A = list(map(int, (input().split())))
g = Graph(N)
for i in range(N):
    g.add_edge(i, A[i]-1)

scc = g.find_scc()
# print("強連結成分:")
# for component in scc:
#     print(component)
ans = 0
for component in scc:
    if len(component)==1: continue
    ans += len(component)
for i in range(N):
    if A[i]-1==i:
        ans += 1
print(ans)


# https://atcoder.jp/contests/typical90/tasks/typical90_u

# N, M = map(int, input().split())

# used = [False] * N
# G = [[] for _ in range(N)]
# H = [[] for _ in range(N)]
# I = []
# cnts = 0

# for i in range(M):
#     a, b = map(int, input().split())
#     G[a-1].append(b-1)
#     H[b-1].append(a-1)

# def dfs(pos):
#     used[pos] = True
#     for i in G[pos]:
#         if used[i] is False: dfs(i)
#     I.append(pos)
#     return

# def dfs2(pos):
#     global cnts
#     used[pos] = True
#     cnts += 1
#     for i in H[pos]:
#         if used[i] is False: dfs2(i)
#     return

# for i in range(N):
#     if used[i] is False: dfs(i)

# ans = 0
# I.reverse()
# used = [False] * N
# for i in I:
#     if used[i]: continue
#     cnts = 0
#     dfs2(i)
#     ans += cnts * (cnts - 1) // 2

# print(ans)
