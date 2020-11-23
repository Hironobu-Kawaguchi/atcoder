# AtCoder Python環境

import networkx as nx
G = nx.Graph()
n, m = map(int, input().split())
G.add_nodes_from(range(n))
for i in range(m):
    a, b = map(int, input().split())
    G.add_edge(a-1, b-1)
# print(G.nodes)
# print(G.edges)
print(nx.number_connected_components(G) - 1)
