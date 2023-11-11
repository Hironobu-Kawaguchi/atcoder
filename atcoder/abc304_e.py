# https://atcoder.jp/contests/abc304/tasks/abc304_e
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

class UnionFind():
    """ Union-Find木の実装（ランクあり） """
    def __init__(self, n):
        self.n = n
        self.parent = [-1]*(n+1)    # parent 親 マイナスだったら根で、絶対値が集合の数
        self.rank   = [0]*(n+1)     # rank 深さ

    def root(self, x):
        """ 木の根を求める """
        if self.parent[x] < 0:      # xが根
            return x
        else:
            self.parent[x] = self.root(self.parent[x])  # 経路圧縮
            return self.parent[x]
            
    def unite(self, x, y):
        """ xとyの属する集合を併合 """
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return 0
        elif self.rank[x] > self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def isSame(self, x, y):
        """ xとyが同じ集合に属するか否か """
        return self.root(x) == self.root(y) or x==y
    
    def size(self, x):
        """ xと同じ集合に属する数 """
        return -self.parent[self.root(x)]


N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    uf.unite(u, v)

K = int(input())
ignore_root_pair = set()
for i in range(K):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    root1, root2 = uf.root(x), uf.root(y)
    if root1 == root2: continue
    if root1 > root2: root1, root2 = root2, root1
    ignore_root_pair.add((root1, root2))

Q = int(input())
for qi in range(Q):
    p, q = map(int, input().split())
    p -= 1; q -= 1
    rootp, rootq = uf.root(p), uf.root(q)
    if rootp > rootq: rootp, rootq = rootq, rootp
    if (rootp, rootq) in ignore_root_pair:
        print("No")
    else:
        print("Yes")
