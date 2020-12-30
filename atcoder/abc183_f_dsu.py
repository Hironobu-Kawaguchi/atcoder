# https://atcoder.jp/contests/abc183/tasks/abc183_f
# https://atcoder.jp/contests/abc183/submissions/18111510

from collections import defaultdict

class dsu:
	def __init__(self,n):
		self.cnt=[1]*n
		self.root=list(range(n))
	def unite(self,x,y):
		x=self.root[x]
		y=self.root[y]
		if x!=y:
			if self.cnt[x]<self.cnt[y]:
				x,y=y,x
			self.cnt[x]+=self.cnt[y]
			self.root[y]=x
		return x
	def leader(self,x):
		if self.root[x]==x:
			return x
		self.root[x]=self.leader(self.root[x])
		return self.root[x]

N,Q = map(int,input().split())
member = [defaultdict(int) for _ in range(N)]
for i,c in enumerate(map(int,input().split())):
	member[i][c-1] = 1
d = dsu(N)

for _ in range(Q):
	t,x,y = map(int,input().split())
	x -= 1
	y -= 1
	if t==1:
		x = d.leader(x)
		y = d.leader(y)
		if x!=y:
			r = d.unite(x,y)
			if r!=x:
				x, y = y, x
			for key, value in member[y].items():
				member[x][key] += value
	else:
		print(member[d.leader(x)][y])
