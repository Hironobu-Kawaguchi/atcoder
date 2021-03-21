# https://atcoder.jp/contests/abc157/tasks/abc157_d

from collections import defaultdict
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()

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
# friend = [[0]*N for _ in range(N)]
friend = defaultdict(lambda : 1)
uf = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    friend[A] += 1
    friend[B] += 1
    uf.unite(A, B)

# block = [[0]*N for _ in range(N)]
block = defaultdict(int)
for j in range(K):
    C, D = map(int, input().split())
    if uf.isSame(C, D):
        block[C] += 1
        block[D] += 1

ans = [0] * (N+1)
for i in range(1, N+1):
    ans[i] = uf.size(i) - friend[i] - block[i]
print(*ans[1:])
