# https://atcoder.jp/contests/arc111/tasks/arc111_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
import networkx as nx

G = nx.Graph()
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    G.add_edge(a,b)
ans = 0
for c in nx.connected_components(G):
    # print(c)
    sg = nx.subgraph(G,c)
    # print(len(sg.nodes), len(sg.edges))
    ns = len(sg.nodes)
    es = len(sg.edges)
    if ns==es+1:  # 木
        ans += ns - 1
    else:         # 木以外
        ans += ns
print(ans)



# WA
# N = int(input())
# a, b = [], []
# s = set()
# dup = set()
# for i in range(N):
#     _a, _b = map(int, input().split())
#     if _a==_b:
#         dup.add(_a)
#     else:
#         a.append(_a)
#         b.append(_b)
#         s.add(_a)
#         s.add(_b)
# cnt = 0
# for _a, _b in zip(a,b):
#     if _a in dup and _b in dup: continue
#     cnt += 1

# ans = min(cnt + len(dup), len(s | dup))
# print(ans)

