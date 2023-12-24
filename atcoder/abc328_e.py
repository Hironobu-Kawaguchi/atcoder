# https://atcoder.jp/contests/abc328/tasks/abc328_e

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

from itertools import combinations

# https://atcoder.jp/contests/atc001/tasks/unionfind_a

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

N, M, K = map(int, input().split())

E = []
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    E.append((u, v, w))

ans = K
for e in combinations(range(M), N-1):
    # print(e, file=sys.stderr)
    uf = UnionFind(N)
    total = 0
    for j in e:
        u, v, w = E[j]
        uf.unite(u, v)
        total += w
    if uf.size(0) == N:
        ans = min(ans, total%K)

print(ans)
