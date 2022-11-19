# https://atcoder.jp/contests/abc276/tasks/abc276_e


import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from itertools import combinations

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

vx = [-1, 1, 0, 0]
vy = [ 0, 0, 1,-1]
H, W = map(int, input().split())
C = [input() for _ in range(H)]
# print(C)

for i in range(H):
    for j in range(W):
        if C[i][j]=='S':
            sx = i
            sy = j
            break
# print(si, sj)
cand = []
for j in range(4):
    nx = sx + vx[j]
    if nx<0 or nx>=H: continue
    ny = sy + vy[j]
    if ny<0 or ny>=W: continue
    if C[nx][ny]!='.': continue
    cand.append(nx*W+ny)
# print(cand)

uf = UnionFind(H*W)

for i in range(H*W):
    x, y = divmod(i, W)
    if C[x][y]!='.': continue
    for j in range(4):
        nx = x + vx[j]
        if nx<0 or nx>=H: continue
        ny = y + vy[j]
        if ny<0 or ny>=W: continue
        if C[nx][ny]!='.': continue
        uf.unite(i, nx*W+ny)

ans = "No"
for i, j in combinations(cand, 2):
    # print(i, j)
    if uf.isSame(i, j):
        ans = "Yes"
        break
print(ans)




# TLE
# import sys
# # input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

# H, W = map(int, input().split())
# C = [input() for _ in range(H)]
# # print(C)

# for i in range(H):
#     for j in range(W):
#         if C[i][j]=='S':
#             si = i
#             sj = j
#             break
# # print(si, sj)

# vi = [-1, 1, 0, 0]
# vj = [ 0, 0, 1,-1]

# ans = "No"

# gone = [[False]*W for _ in range(H)]

# def dfs(i, j, n):
#     global ans
#     if i==si and j==sj and n>=4:
#         ans = "Yes"
#         return
#     for idx in range(4):
#         ni = i + vi[idx]
#         if ni<0 or ni>=H: continue
#         nj = j + vj[idx]
#         if nj<0 or nj>=W: continue
#         if C[ni][nj]=='#': continue
#         if gone[ni][nj]: continue
#         gone[ni][nj] = True
#         dfs(ni, nj, n+1)
#         gone[ni][nj] = False
#     return

# dfs(si, sj, 0)
# print(ans)

