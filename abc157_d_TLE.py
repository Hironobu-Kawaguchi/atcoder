# https://atcoder.jp/contests/abc157/tasks/abc157_d

import sys
input = sys.stdin.buffer.readline

class UnionFind():
    """ Union-Find木の実装（ランクあり） """
    def __init__(self, n):
        self.n = n
        self.parent = [-1]*(n+1)    # parent 親
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
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def isSame(self, x, y):
        """ xとyが同じ集合に属するか否か """
        return self.root(x) == self.root(y) or x==y

N, M, K = map(int, input().split())
friend = [[0]*N for _ in range(N)]
block = [[0]*N for _ in range(N)]
uf = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    friend[A-1][B-1] = 1
    friend[B-1][A-1] = 1
    uf.unite(A-1, B-1)
for j in range(K):
    C, D = map(int, input().split())
    block[C-1][D-1] = 1
    block[D-1][C-1] = 1

for i in range(N):
    ans = 0
    for j in range(N):
        if i == j:
            continue
        elif uf.isSame(i,j) and friend[i][j] == 0 and block[i][j] == 0:
            ans += 1
    print(ans, end= ' ')
