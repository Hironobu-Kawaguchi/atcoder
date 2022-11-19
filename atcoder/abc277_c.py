# https://atcoder.jp/contests/abc277/tasks/abc277_b

from collections import defaultdict, deque

n = int(input())
G = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

que = deque([1])
st = set([1])

while que:
    u = que.popleft()
    for v in G[u]:
        if v not in st:
            que.append(v)
            st.add(v)
print(max(st))


# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)

# class UnionFind():
#     """ Union-Find木の実装（ランクあり） """
#     def __init__(self, n):
#         self.n = n
#         self.parent = [-1]*(n+1)    # parent 親 マイナスだったら根で、絶対値が集合の数
#         self.rank   = [0]*(n+1)     # rank 深さ

#     def root(self, x):
#         """ 木の根を求める """
#         if self.parent[x] < 0:      # xが根
#             return x
#         else:
#             self.parent[x] = self.root(self.parent[x])  # 経路圧縮
#             return self.parent[x]
            
#     def unite(self, x, y):
#         """ xとyの属する集合を併合 """
#         x = self.root(x)
#         y = self.root(y)
#         if x == y:
#             return 0
#         elif self.rank[x] > self.rank[y]:
#             self.parent[x] += self.parent[y]
#             self.parent[y] = x
#         else:
#             self.parent[y] += self.parent[x]
#             self.parent[x] = y
#             if self.rank[x] == self.rank[y]:
#                 self.rank[y] += 1

#     def isSame(self, x, y):
#         """ xとyが同じ集合に属するか否か """
#         return self.root(x) == self.root(y) or x==y
    
#     def size(self, x):
#         """ xと同じ集合に属する数 """
#         return -self.parent[self.root(x)]

# N = int(input())
# st = set()
# AB = []
# for i in range(N):
#     a, b = map(int, input().split())
#     AB.append((a, b))
#     st.add(a)
#     st.add(b)
# lst = sorted(list(st))
# M = len(st)
# d = dict(zip(lst, range(M)))
# # print(d)
# # print(lst)

# uf = UnionFind(M)
# for i in range(N):
#     a, b = AB[i]
#     uf.unite(d[a], d[b])

# if lst[0]!=1:
#     ans = 1
# else:
#     for j in range(M-1, -1, -1):
#         if uf.isSame(d[1], d[lst[j]]):
#             ans = lst[j]
#             break
# print(ans)

