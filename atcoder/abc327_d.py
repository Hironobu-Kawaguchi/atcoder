# https://atcoder.jp/contests/abc327/tasks/abc327_d

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M):
    G[A[i]-1].append(B[i]-1)
    G[B[i]-1].append(A[i]-1)

def is_bipartite(graph):
    color = [-1] * N  # -1 means uncolored, 0 and 1 are the two colors
    
    for start in range(N):
        if color[start] == -1:  # if the node is uncolored
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # if the neighbor is uncolored
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # if the neighbor has the same color as the current node
                        return False  # the graph is not bipartite
    
    return True

if is_bipartite(G):
    print('Yes')
else:
    print('No')
