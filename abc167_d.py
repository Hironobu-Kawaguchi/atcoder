# https://atcoder.jp/contests/abc167/tasks/abc167_d

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
A = list(map(int, (input().split())))

done = [0]*N
now = 0
cnt = 1
while True:
    if done[now] != 0:
        start = done[now] - 1
        cycle = cnt - start - 1
        break
    else:
        done[now] = cnt
        now = A[now]-1
        cnt += 1
if K>=start:
    K -= start
    K %= cycle
else:
    now = 0
for _ in range(K):
    now = A[now]-1
print(now+1)
# print(start, cycle, now, done)

# class UnionFind():
#     """ Union-Find木の実装（ランクあり） """
#     def __init__(self, n):
#         self.n = n
#         self.parent = [-1]*(n+1)    # parent 親 マイナスだったら根で、絶対値が集合の数
#         self.rank   = [0]*(n+1)     # rank 深さ

#     def root(self, x):
#         """ 木の根を求める """
#         if self.parent[x] < 0:      # xが根
#             return x
#         else:
#             self.parent[x] = self.root(self.parent[x])  # 経路圧縮
#             return self.parent[x]
            
#     def unite(self, x, y):
#         """ xとyの属する集合を併合 """
#         x = self.root(x)
#         y = self.root(y)
#         if x == y:
#             return 0
#         elif self.rank[x] > self.rank[y]:
#             self.parent[x] += self.parent[y]
#             self.parent[y] = x
#         else:
#             self.parent[y] += self.parent[x]
#             self.parent[x] = y
#             if self.rank[x] == self.rank[y]:
#                 self.rank[y] += 1

#     def isSame(self, x, y):
#         """ xとyが同じ集合に属するか否か """
#         return self.root(x) == self.root(y) or x==y
    
#     def size(self, x):
#         """ xと同じ集合に属する数 """
#         return -self.parent[self.root(x)]

# N, K = map(int, input().split())
# A = list(map(int, (input().split())))

# uf = UnionFind(N)
# for i in range(N):
#     uf.unite(i, A[i]-1)

# now = 0
# K %= uf.size(now)
# for _ in range(K):
#     now = A[now]-1
# print(now+1)




# N = int(input())
# S = input()
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
