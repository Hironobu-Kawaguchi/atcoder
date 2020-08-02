# https://atcoder.jp/contests/arc030/tasks/arc030_2

n, x = map(int, input().split())
x -= 1
h = list(map(int, input().split()))
G = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].add(b)
    G[b].add(a)
deg = [len(s) for s in G]   # 各頂点の次数 全ての頂点に行く場合は、この合計が答え

deg1_list = [y for y in range(n) if deg[y] == 1]    # 次数1本の頂点

# for y in deg1_list:
while deg1_list:
    y = deg1_list.pop()
    if y == x: continue     # スタート地点は残す
    if h[y] == 1: continue  # 宝石がある頂点は残す
    deg[y] = 0  # 行かない頂点yの次数を0に
    for z in G[y]:  # 頂点yに隣接する頂点z
        G[z].remove(y)  # 頂点yとの辺を削除
        deg[z] -= 1     # zの次元数を1減らす
        if deg[z] == 1:
            deg1_list.append(z)
ans = sum(deg)
print(ans)
