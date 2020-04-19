# https://atcoder.jp/contests/abc157/tasks/abc157_d
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)


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
uf = UnionFind(N)
friends = [[] for _ in range(N)]
blocks = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1; B -= 1
    uf.unite(A, B)
    friends[A].append(B)
    friends[B].append(A)
for i in range(K):
    C, D = map(int, input().split())
    C -= 1; D -= 1
    blocks[C].append(D)
    blocks[D].append(C)

ans = [0] * N
for i in range(N):
    ans[i] = uf.size(i) - 1   # 自分を除外
    ans[i] -= len(friends[i]) # 既に友達を除外
    block_num = 0
    for j in blocks[i]:
        if uf.isSame(i,j):
            block_num += 1
    ans[i] -= block_num

print(*ans)
