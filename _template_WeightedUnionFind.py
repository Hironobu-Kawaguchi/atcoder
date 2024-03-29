# https://atcoder.jp/contests/abc328/tasks/abc328_f
# https://github.com/Ueeek/Lib/blob/master/WeightedUnionFind.py

import sys

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
