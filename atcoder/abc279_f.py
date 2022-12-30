# https://atcoder.jp/contests/ABC279/tasks/abc279_e
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
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


N, Q = map(int, input().split())
box = dict(zip(range(N), range(N)))
roots = dict(zip(range(N), range(N)))
# print(box)
uf = UnionFind(N+Q)
now = N
for i in range(Q):
    query = input()
    # print(query)
    if query[0]=='1':
        t, x, y = map(int, query.split())
        if box[y-1]==-1:
            continue
        elif box[x-1]==-1:
            rt = box[y-1]
        else:
            uf.unite(box[y-1], box[x-1])
            rt = uf.root(box[x-1])
        box[x-1] = rt
        roots[rt] = x-1
        box[y-1] = -1
    elif query[0]=='2':
        t, x = map(int, query.split())
        uf.unite(now, box[x-1])
        rt = uf.root(now)
        box[x-1] = rt
        roots[rt] = x-1
        now += 1
        # print(now, rt)
    else:
        t, x = map(int, query.split())
        rt = uf.root(x-1)
        # print(x-1, rt, box, roots)
        print(roots[rt]+1)
    # print(now, box)





# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
