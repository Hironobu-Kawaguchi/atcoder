# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bg
# https://github.com/E869120/kyopro-tessoku
# https://atcoder.jp/contests/abc185/tasks/abc185_f
# https://qiita.com/takayg1/items/c811bd07c21923d7ec69

#####segfunc#####
def segfunc(x, y):
    return x+y
#################

#####ide_ele#####
ide_ele = 0
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, p):
        return self.tree[self.num + p]

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

# 入力
N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]

# クエリの処理
A = [0]*N
Z = SegTree(A, segfunc, ide_ele)
for q in queries:
	tp, *cont = q
	if tp == 1:
		pos, x = cont
		Z.update(pos - 1, x) # pos は 1-indexed で入力されるので、update 関数の引数は pos - 1 にします
	if tp == 2:
		l, r = cont
		answer = Z.query(l - 1, r - 1) # 0-indexed の実装では、最初のセルに対応する半開区間は [0, size) です
		print(answer)



# # セグメント木（ここでは書籍とは異なり、pos が 0-indexed になるように実装しています）
# class segtree:
# 	# 要素 dat の初期化を行う（最初は全部ゼロ）
# 	def __init__(self, n):
# 		self.size = 1
# 		while self.size < n:
# 			self.size *= 2
# 		self.dat = [ 0 ] * (self.size * 2)
	
# 	# クエリ 1 に対する処理
# 	def update(self, pos, x):
# 		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
# 		self.dat[pos] = x
# 		while pos >= 2:
# 			pos //= 2
# 			self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1] # 8.8 節から変更した部分
	
# 	# クエリ 2 に対する処理
# 	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
# 	def query(self, l, r, a, b, u):
# 		if r <= a or b <= l:
# 			return 0 # 8.8 節から変更した部分
# 		if l <= a and b <= r:
# 			return self.dat[u]
# 		m = (a + b) // 2
# 		answerl = self.query(l, r, a, m, u * 2)
# 		answerr = self.query(l, r, m, b, u * 2 + 1)
# 		return answerl + answerr # 8.8 節から変更した部分

# # 入力
# N, Q = map(int, input().split())
# queries = [ list(map(int, input().split())) for i in range(Q) ]

# # クエリの処理
# Z = segtree(N)
# for q in queries:
# 	tp, *cont = q
# 	if tp == 1:
# 		pos, x = cont
# 		Z.update(pos - 1, x) # pos は 1-indexed で入力されるので、update 関数の引数は pos - 1 にします
# 	if tp == 2:
# 		l, r = cont
# 		answer = Z.query(l - 1, r - 1, 0, Z.size, 1) # 0-indexed の実装では、最初のセルに対応する半開区間は [0, size) です
# 		print(answer)