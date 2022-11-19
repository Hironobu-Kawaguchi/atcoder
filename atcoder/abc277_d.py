# https://atcoder.jp/contests/abc277/tasks/abc277_d


import sys
input = sys.stdin.buffer.readline

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
A = list(map(int, (input().split())))
A.sort()

uf = UnionFind(N)
for i in range(N):
    j = (i+1)%N
    if (A[i]==A[j] or (A[i]+1)%M==A[j]):
        uf.unite(i, j)
s = [0]*N
for i in range(N):
    s[uf.root(i)] += A[i]
mx = 0
for i in range(N):
    mx = max(mx, s[i])
print(sum(A) - mx)


# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# from collections import defaultdict, Counter

# N, M = map(int, input().split())
# A = list(map(int, (input().split())))
# # md =[]
# sm = 0
# original = dict()
# st = set()
# for i in range(N):
#     tmp = (A[i]+1)%M
#     # md.append(tmp)
#     # sm += A[i]
#     # st.add(A[i])
#     # st.add(md[i])
#     if tmp not in original:
#         original[tmp] = set([A[i]])
#     else:
#         original[tmp].add(A[i])
# cnt = Counter(A)
# print(sorted(cnt.items(), key = lambda item: item[0]))
# print(A)
# # print(md)
# # print(sm)
# print(original)
# # K = len(st)

# lst = sorted(cnt.keys())
# print(lst)
# K = len(lst)
# d = dict(zip(lst, range(K)))
# print(d)

# to = [[] for _ in range(K)]
# for i in range(K):
#     tmp = (lst[i]+1)%M
#     if tmp in cnt:
#         to[i].append


# memo = [0] * K

# def def():
#     return

# for k, v in cnt.items():





# lst = sorted(list(st))
# print(lst)
# print(d)
# cnt = defaultdict(int)
# for j in range(N):
#     tmp = (A[i]+1)%M
#     for v in list(original[tmp]):
#         cnt[v] += A[i]
#     if A[j]!=md[j]:
#         cnt[md[j]] += A[j]
# print(cnt)
# ans = 0
# for k, v in cnt.items():
#     ans = max(ans, cnt[k])
# print(sm - ans)



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
