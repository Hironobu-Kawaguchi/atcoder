# https://atcoder.jp/contests/abc328/tasks/abc328_f

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

class WeightedUnionFind:
    """
    重み付きUnion Find
    """

    def __init__(self, n):
        """
        :param:n size of nodes

        par : show parent of each node
        rank : show height
        weight: dist from root to the node
        """
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)

    def find(self, x):
        """
        :param: x=> search parent of node x
        """
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w):
        """
        x: node
        y: node
        w: weight

        Union
        w->weight from x to y
        """
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        """
        x:node
        y: node

        Are x ,y in same Group?
        bool
        """
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        """
        x: node
        y: node

        x->yのcost
        """
        return self.weight[x] - self.weight[y]

N, Q = map(int, input().split())

ans = []
uf = WeightedUnionFind(N)
for qi in range(Q):
    a, b, d = map(int, input().split())
    a -= 1; b -= 1
    # print(qi+1, a, b, d, file=sys.stderr)
    if a==b:        # a=bのときはd=0でないといけない
        if d!=0: continue
    elif uf.same(a, b):
        diff = uf.diff(a, b)
        # print(diff, file=sys.stderr)
        if diff != d: continue  # 差が異なる時はダメ
    uf.union(a, b, d)
    ans.append(qi+1)
ans.sort()
print(*ans)





# # https://atcoder.jp/contests/atc001/tasks/unionfind_a

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


# INF = 10**18
# N, Q = map(int, input().split())

# ans = []
# G = [[] for _ in range(N)]
# dist = [INF] * N
# start_flg = True    # 最初はdist=0にする
# uf = UnionFind(N)
# # fitting = {}     # 調整するエッジを記録
# for qi in range(Q):
#     a, b, d = map(int, input().split())
#     a -= 1; b -= 1
#     if a==b:        # a=bのときはd=0でないといけない
#         if d!=0: continue
#     elif start_flg:
#         dist[a] = 0   # 最初はdist=0にする
#         dist[b] = d
#     else:
#         if dist[a]==INF and dist[b]!=INF:   # aが既に確定しているとき
#             dist[a] = dist[b] - d
#         elif dist[a]!=INF and dist[b]==INF: # bが既に確定しているとき
#             dist[b] = dist[a] + d
#         elif dist[a]!=INF and dist[b]!=INF: # a,bが既に確定しているとき
#             # if (min(a,b), max(a,b)) in fitting: # 以前に調整したエッジのとき
#             #     if a < b and fitting[(a,b)] != dist[b] - dist[a] - d: continue
#             #     if a > b and fitting[(b,a)] != dist[b] - dist[a] - d: continue
#             if dist[b] - dist[a] != d:
#                 if uf.isSame(a, b):
#                     continue
#                 else:       # 結合するので，値を調整する
#                     diff = dist[b] - dist[a] - d
#                     # if a < b:
#                     #     fitting[(a,b)] = diff
#                     # else:
#                     #     fitting[(b,a)] = -diff
#                     for j in range(N):          # TLE
#                         if uf.isSame(a, j):
#                             dist[j] += diff
#         else:                               # a,bが未確定のとき
#             dist[a] = 0   # 仮でdist=0にする．他と結合するときに調整する
#             dist[b] = d
#     uf.unite(a, b)
#     ans.append(qi+1)
#     G[a].append((b, d))
#     G[b].append((a, -d))
#     # print(*ans, " ", *dist, file=sys.stderr)
#     start_flg = False

# ans.sort()
# print(*ans)
# # print(*dist, file=sys.stderr)
