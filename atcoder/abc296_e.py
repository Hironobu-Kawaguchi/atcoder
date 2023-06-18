# https://atcoder.jp/contests/abc296/tasks/abc296_e

from typing import List, Tuple
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)

    def dfs(self, v: int, visited: List[bool], result: List[int]):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, result)
        result.append(v)

    def dfs_transpose(self, v: int, visited: List[bool], component: List[int]):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_transpose(i, visited, component)

    def transpose(self) -> "Graph":
        gt = Graph(self.V)
        for i in range(self.V):
            for j in self.graph[i]:
                gt.add_edge(j, i)
        return gt

    def find_scc(self) -> List[List[int]]:
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



# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# from collections import deque
# import time
# start_time = time.time()
# order_count = [0, 0.0]

# def main():
#     N = int(input())
#     A = list(map(int, (input().split())))
#     to = [-1] * N
#     for i in range(N):
#         to[i] = A[i] - 1
#     # print(to)

#     wins = [0] * N

#     def round(i):
#         visited = set()   ### これをリスト管理するとO(N^2)になりTLE
#         q = deque([i])
#         while q:
#             v = q.popleft()
#             # print("round", i+1, v+1)
#             order_count[0] += 1
#             wins[v] = 1
#             if v in visited:
#                 break
#             visited.add(v)
#             u = to[v]
#             if u in visited:
#                 continue
#             q.append(u)
#         return

#     visited = [False] * N
#     for i in range(N):
#         if visited[i]: continue
#         # if wins[i]: continue
#         # print(i, order_count[0], time.time() - start_time, order_count[1])
#         start_time_set = time.time()
#         visited_in = set()   ### これをリスト管理するとO(N^2)になりTLE
#         order_count[1] += time.time() - start_time_set
#         q = deque([i])
#         while q:
#             v = q.popleft()
#             # print(i+1, v+1)
#             order_count[0] += 1
#             if visited[v]:
#                 start_time_set = time.time()
#                 if v in visited_in:
#                     round(v)
#                     order_count[1] += time.time() - start_time_set
#                     # print(wins)
#                 break
#             visited[v] = True
#             start_time_set = time.time()
#             visited_in.add(v)
#             order_count[1] += time.time() - start_time_set
#             order_count[0] += len(visited_in)
#             u = to[v]
#             q.append(u)
#     # print(wins)
#     ans = 0
#     for i in range(N):
#         if wins[i]:
#             ans += 1
#     print(ans)
#     return

# main()
