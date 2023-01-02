# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bo
# https://github.com/E869120/kyopro-tessoku
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

# 入力
N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

# 辺を長さの小さい順にソートする
edges.sort(key = lambda x: x[2])

# 最小全域木を求める
uf = UnionFind(N)
answer = 0
for a, b, c in edges:
	if not uf.isSame(a, b):
		uf.unite(a, b)
		answer += c

# 答えの出力
print(answer)




# # Union-Find 木
# class unionfind:
# 	# n 頂点の Union-Find 木を作成
# 	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
# 	def __init__(self, n):
# 		self.n = n
# 		self.par = [ -1 ] * (n + 1) # 最初は親が無い
# 		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1
	
# 	# 頂点 x の根を返す関数
# 	def root(self, x):
# 		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
# 		while self.par[x] != -1:
# 			x = self.par[x]
# 		return x
	
# 	# 要素 u, v を統合する関数
# 	def unite(self, u, v):
# 		rootu = self.root(u)
# 		rootv = self.root(v)
# 		if rootu != rootv:
# 			# u と v が異なるグループのときのみ処理を行う
# 			if self.size[rootu] < self.size[rootv]:
# 				self.par[rootu] = rootv
# 				self.size[rootv] += self.size[rootu]
# 			else:
# 				self.par[rootv] = rootu
# 				self.size[rootu] += self.size[rootv]
	
# 	#  要素 u と v が同一のグループかどうかを返す関数
# 	def same(self, u, v):
# 		return self.root(u) == self.root(v)

# # 入力
# N, M = map(int, input().split())
# edges = [ list(map(int, input().split())) for i in range(M) ]

# # 辺を長さの小さい順にソートする
# edges.sort(key = lambda x: x[2])

# # 最小全域木を求める
# uf = unionfind(N)
# answer = 0
# for a, b, c in edges:
# 	if not uf.same(a, b):
# 		uf.unite(a, b)
# 		answer += c

# # 答えの出力
# print(answer)