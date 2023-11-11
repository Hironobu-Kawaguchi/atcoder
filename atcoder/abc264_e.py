# https://atcoder.jp/contests/abc264/tasks/abc264_e
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

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

N, M, E = map(int, input().split())
U, V = [], []
for i in range(E):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    U.append(u)
    V.append(v)

Q = int(input())
flg = [True] * E
X = []
for i in range(Q):
    x = int(input())
    x -= 1
    flg[x] = False
    X.append(x)

uf = UnionFind(N + M)
w = [False] * (N + M)                   # 集合に発電所があれば1，なければ0
for i in range(N, N + M): w[i] = True   # N番目以降は発電所
cur = 0
for i in range(E):
    if flg[i]:          # 切れない電線のみ繋ぐ
        if uf.isSame(U[i], V[i]): continue
        fu = w[uf.root(U[i])]   # 集合に発電所があれば1，なければ0
        fv = w[uf.root(V[i])]   # 集合に発電所があれば1，なければ0
        if (fu==0 and fv==1): cur += uf.size(U[i])  # 発電所がなく，全て都市だったU[i]の集合を繋ぐので，都市数を足す
        if (fu==1 and fv==0): cur += uf.size(V[i])  # 発電所がなく，全て都市だったV[i]の集合を繋ぐので，都市数を足す
        uf.unite(U[i], V[i])            # 集合を繋ぐ
        w[uf.root(U[i])] = max(fu, fv)  # 集合に発電所があれば1，なければ0
# print(*w, file=sys.stderr)

ans = []
for i in range(Q-1, -1, -1):    # 電源を切る順番を逆から見て，電源を繋いでいく場合で評価する
    ans.append(cur)     # 電線を切る前の電気が通っている都市の数を記録
    x = X[i]
    if uf.isSame(U[x], V[x]): continue  # 電線が切れても集合が繋がっているならスルー
    fu = w[uf.root(U[x])]       # 集合に発電所があれば1，なければ0
    fv = w[uf.root(V[x])]       # 集合に発電所があれば1，なければ0
    if (fu==0 and fv==1): cur += uf.size(U[x])  # 発電所がなく，全て都市だったU[x]の集合を繋ぐので，都市数を足す
    if (fu==1 and fv==0): cur += uf.size(V[x])  # 発電所がなく，全て都市だったV[x]の集合を繋ぐので，都市数を足す
    uf.unite(U[x], V[x])            # 集合を繋ぐ
    w[uf.root(U[x])] = max(fu, fv)  # 集合に発電所があれば1，なければ0
ans.reverse()
print(*ans, sep='\n')
