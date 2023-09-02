# https://atcoder.jp/contests/abc317/tasks/abc317_c

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

# ノード数N, エッジ数M
N, M = map(int, input().split())

# グラフを表現する辞書。キーはノード、値はエッジとその重みのリスト。
graph = {}
for _ in range(M):
    a, b, w = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, w))
    graph[b].append((a, w))  # 無向グラフなので、逆方向も追加

# DFSで最大の重みの和を求める
def dfs(node, weight_sum):
    max_weight = weight_sum
    
    for next_node, edge_weight in graph.get(node, []):
        if visited[next_node]: continue
        visited[next_node] = True
        max_weight = max(max_weight, dfs(next_node, weight_sum + edge_weight))
        visited[next_node] = False
            
    return max_weight

# すべてのノードからスタートして、最大の重みの和を求める
max_weight_global = 0
for start_node in range(1, N+1):
    visited = [False] * (N+1)
    visited[start_node] = True
    max_weight_global = max(max_weight_global, dfs(start_node, 0))

print(max_weight_global)
