# https://atcoder.jp/contests/typical90/tasks/typical90_l
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


H, W = map(int, input().split())
Q = int(input())

uf = UnionFind(H*W)
col = [False] * (H*W)

for qi in range(Q):
    q = input()
    # print(q)
    if q[0]=='1':
        t, r, c = map(int, q.split())
        r -= 1; c -= 1
        idx = r * W + c
        col[idx] = True
        for mov in [-W, -1, 1, W]:
            if idx+mov<0 or idx+mov>=H*W: continue
            if (idx+1)%W==0 and mov==1: continue
            if idx%W==0 and mov==-1: continue
            if col[idx+mov]:
                uf.unite(idx, idx+mov)
    else:
        t, ra, ca, rb, cb = map(int, q.split())
        ra -= 1; ca -= 1; rb -= 1; cb -= 1
        idxa = ra * W + ca
        idxb = rb * W + cb
        if col[idxa] and col[idxb] and uf.isSame(idxa, idxb):
            print("Yes")
        else:
            print("No")



# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
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
