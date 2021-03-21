# https://atcoder.jp/contests/arc032/tasks/arc032_2

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
    a,b = map(int, input().split())
    uf.unite(a-1, b-1)

ans = -1
for i in range(N):
    if uf.root(i) == i:
        ans += 1
print(ans)
