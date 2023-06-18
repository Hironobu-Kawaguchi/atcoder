# https://atcoder.jp/contests/ahc020/tasks/ahc020_a

import sys
input = sys.stdin.buffer.readline
import math
import random
import time
import copy
start = time.time()
INF = 1001001001

# 二次元の点を扱うクラス
class point2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	# 2 点間の距離を求める関数
	def dist(self, p):
		return math.ceil(((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5)

# 重みつきエッジを扱うクラス
class edge:
	def __init__(self, u, v, w, idx):
		self.u = u
		self.v = v
		self.w = w
		self.idx = idx

# Union-Find 木
class unionfind:
	# n 頂点の Union-Find 木を作成
	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 最初は親が無い
		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1
	
	# 頂点 x の根を返す関数
	def root(self, x):
		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
		while self.par[x] != -1:
			x = self.par[x]
		return x
	
	# 要素 u, v を統合する関数
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			# u と v が異なるグループのときのみ処理を行う
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]
	
	#  要素 u と v が同一のグループかどうかを返す関数
	def same(self, u, v):
		return self.root(u) == self.root(v)

# 重み付き平面無向グラフのクラス
class Graph:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.nodes = []
        self.edges = []
        self.to = [[] for _ in range(N)]
    def add_node(self, x, y):
        p = point2d(x, y)
        self.nodes.append(p)
    def add_edge(self, u, v, w, idx):
        e = edge(u, v, w, idx)
        self.edges.append(e)
        self.to[u].append((v, w, idx))
        self.to[v].append((u, w, idx))
    # 最小全域木を求める関数
    def kruskal(self):
        B = [0] * M
        self.edges.sort(key = lambda x: x.w)
        uf = unionfind(self.N)
        for e in self.edges:
            if not uf.same(e.u, e.v):
                uf.unite(e.u, e.v)
                B[e.idx] = 1
        return B
    def num_edge(self, i, B):
        cnt = 0
        edges = []
        for v, w, idx in self.to[i]:
            if B[idx] == 1:
                cnt += 1
                edges.append(idx)
        return cnt, edges

N, M, K = map(int, input().split())
G = Graph(N, M)
for i in range(N):
    x, y = map(int, input().split())
    G.add_node(x, y)
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    G.add_edge(u, v, w, i)

ab = []
for i in range(K):
    a, b = map(int, input().split())
    p = point2d(a, b)
    ab.append(p)

def calc_cost(P, B):
    cost = 0
    for i in range(N):
        cost += P[i] * P[i]
    for i in range(M):
        cost += B[i] * G.edges[i].w
    return cost

def calc_score(P, B):
    n = 0
    for i in range(N):
        for k in range(K):
            if P[i] >= G.nodes[i].dist(ab[k]):
                n += 1
            if n == K: break
        if n == K: break
    # n==Kの場合
    if n==K:
        S = calc_cost(P, B)
        score = round(1e6 * (1 + 1e8 / (S + 1e7)))
        return score, S
    else:
        return round(1e6 * (n + 1) / K), n

# B = [1] * M
B = G.kruskal()

P = [0] * N

for k in range(K):
    bestd = INF
    for i in range(N):
        d = G.nodes[i].dist(ab[k])
        if bestd > d:
            bestd = d
            besti = i
    P[besti] = max(P[besti], math.ceil(bestd))

def check_match(P):
    kichi = [set() for _ in range(N)]
    ie = [set() for _ in range(K)]
    for i in range(N):
        for k in range(K):
            if P[i] >= G.nodes[i].dist(ab[k]):
                kichi[i].add(k)
                ie[k].add(i)
    return kichi, ie

# 他の基地でカバーされている基地を削除する
kichi, ie = check_match(P)
for i in range(N):
    if P[i]==0: continue
    flg = True
    for k in kichi[i]:
        if len(ie[k])==1:
            flg = False
            break
    if flg:
        for k in kichi[i]:
            ie[k].remove(i)
        kichi[i] = set()
        P[i] = 0

# P[i]=0でエッジが1本のみを削除する
while True:
    delcnt = 0
    for i in range(N):
        if i==0: continue
        if P[i]==0:
            cnt, edges = G.num_edge(i, B)
            # cnt = 0
            # for j, w, idx in G.to[i]:
            #     if B[idx]==1:
            #         cnt += 1
            #         ii = idx
            if cnt==1:
                # B[ii] = 0
                B[edges[0]] = 0
                delcnt += 1
    if delcnt==0: break

# # エッジが1本のみの基地を他の基地のP[i]を加算して削除することを検討する
# for i in range(N):
#     if P[i]==0: continue
#     cnt, edges = G.num_edge(i, B)
#     if cnt!=1: continue
#     ie = []
#     for k in range(K):
#         if P[i] >= G.nodes[i].dist(ab[k]):
#             ie.append(k)
#     bestd = 1001001001
#     for j in range(N):
#         if j==i: continue
#         if P[j]==0: continue
#         d = G.nodes[j].dist(ab[ie[0]])**2 - P[j]**2
#         if bestd > d:
#             bestd = d
#             bestj = j
#     pj = P[bestj]
#     for k in ie:
#         pj = max(pj, G.nodes[bestj].dist(ab[k]))
#     if P[i]*P[i]>pj*pj-P[bestj]*P[bestj]:
#         P[bestj] = pj
#         P[i] = 0

# エッジが1本のみの基地を他の基地のP[i]を加算して削除することを検討する
for i in range(N):
    if P[i]==0: continue
    cnt, edges = G.num_edge(i, B)
    if cnt!=1: continue
    ie = []
    for k in range(K):
        if P[i] >= G.nodes[i].dist(ab[k]):
            ie.append(k)
    pj = copy.copy(P)
    flg = False
    for k in ie:
        bestd = INF
        for j in range(N):
            if j==i: continue
            if P[j]==0: continue
            dist = G.nodes[j].dist(ab[k])
            if dist>5000: continue
            d = dist**2 - pj[j]**2
            if bestd > d:
                bestd = d
                bestj = j
        if bestd==INF:
            flg = True
        else:
            pj[bestj] = max(pj[bestj], G.nodes[bestj].dist(ab[k]))
    if flg: continue
    diff = P[i]*P[i]
    for j in range(N):
        if j==i: continue
        if pj[j]==P[j]: continue
        diff -= pj[j]*pj[j] - P[j]*P[j]
    # print(diff, i, j)
    if diff:
        for j in range(N):
            if j==i: continue
            if pj[j]==P[j]: continue
            P[j] = pj[j]
        P[i] = 0

# P[i]=0でエッジが1本のみを削除する
while True:
    delcnt = 0
    for i in range(N):
        if i==0: continue
        if P[i]==0:
            cnt, edges = G.num_edge(i, B)
            # cnt = 0
            # for j, w, idx in G.to[i]:
            #     if B[idx]==1:
            #         cnt += 1
            #         ii = idx
            if cnt==1:
                # B[ii] = 0
                B[edges[0]] = 0
                delcnt += 1
    if delcnt==0: break

# 他の基地でカバーされている基地を削除する
kichi, ie = check_match(P)
for i in range(N):
    if P[i]==0: continue
    flg = True
    for k in kichi[i]:
        if len(ie[k])==1:
            flg = False
            break
    if flg:
        for k in kichi[i]:
            ie[k].remove(i)
        kichi[i] = set()
        P[i] = 0

# # 0以上5000未満の整数をランダムに返す
# for i in range(N):
#     P[i] = random.randrange(5000)

# def search_P(P):
#     bestP = copy.copy(P)
#     bestScore, S = calc_score(P)
#     # 1.5秒whileを回す
#     cnt = 0
#     # now = 5000
#     while time.time() - start < 1.0:
#         # 0以上5000以下の整数をランダムに返す
#         for i in range(N):
#             P[i] = random.randrange(5001)
#         # 1000の倍数を返す
#         # P = [(cnt+1)*1000] * N
#         # if P[0]>5000: break
#         # 5000から1/2ずつ減らす
#         # P = [now] * N
#         # now //= 2
#         score, S = calc_score(P)
#         if score > bestScore:
#             bestP = copy.copy(P)
#             bestScore = score
#         cnt += 1
#     print("search cnt:", cnt, file=sys.stderr)
#     return bestP

# P = search_P(P)

print(*P)
print(*B)

score, S = calc_score(P, B)
print("score:", score, file=sys.stderr)
print("cost:", S, file=sys.stderr)
if max(P)>5000:
    print("P max over", file=sys.stderr)