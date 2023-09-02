# https://atcoder.jp/contests/abc315/tasks/abc315_e
# from numba import njit
# from functools import lru_cache

# DFS 帰りがけ順
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

def dfs(v):
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)
    ans.append(v + 1)

N = int(input())
cp = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(1, len(cp[i])):
        graph[i].append(cp[i][j] - 1)
visited = [False] * N
ans = []
dfs(0)
print(*ans[:-1])



# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
# from collections import deque

# def dfs(v, visited, graph):
#     visited[v] = True
#     for next_node in graph[v]:
#         if not visited[next_node]:
#             dfs(next_node, visited, graph)

# def topological_sort_reverse(graph):
#     # ノード0から到達可能なノードを特定
#     visited = [False] * len(graph)
#     dfs(0, visited, graph)

#     # 入次数の初期化
#     indegree = [0] * len(graph)
#     for i, edges in enumerate(graph):
#         for edge in edges:
#             if visited[i] and visited[edge]:  # 両方のノードが到達可能な場合のみ入次数を増やす
#                 indegree[edge] += 1

#     # 入次数が0のノードをキューに追加
#     queue = deque([i for i, deg in enumerate(indegree) if deg == 0 and visited[i]])
#     result = []

#     # トポロジカルソート
#     while queue:
#         node = queue.popleft()
#         result.append(node)
#         for neighbor in graph[node]:
#             if visited[neighbor]:  # 到達可能なノードのみを考慮
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)

#     return result[::-1]  # 結果を逆順にして返す


# N = int(input())
# cp = [list(map(int, input().split())) for _ in range(N)]
# graph = [[] for _ in range(N)]
# for i in range(N):
#     for j in range(1, len(cp[i])):
#         graph[i].append(cp[i][j] - 1)
# # print(graph, file=sys.stderr)

# ans = topological_sort_reverse(graph)
# for i in range(len(ans)):
#     ans[i] += 1
# print(*ans[:-1])
