# https://atcoder.jp/contests/abc292/tasks/abc292_d
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
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

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    d = [0]*N
    for i in range(M):
        u, v = map(int, input().split())
        uf.unite(u-1, v-1)
        d[u-1] += 1
        d[v-1] += 1
    nodes = [0]*N
    edges = [0]*N
    for i in range(N):
        rt = uf.root(i)
        nodes[rt] += 1
        edges[rt] += d[i]
    for i in range(N):
        if nodes[i]*2!=edges[i]:
            # print(i, nodes[i], edges[i])
            print("No")
            return
    print("Yes")
    return

main()

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
