# https://atcoder.jp/contests/abc139/tasks/abc139_e
# 有向グラフの最長経路問題に置き換えた解法
# DAG: ループなし
# トポロジカルソート

def main():
    n = int(input())
    a = [list(map(lambda x: int(x)-1, input().split())) for _ in range(n)]  # 選手idを0始まりに変換
    id = [[0]*n for _ in range(n)]  # 試合のid=DAGの頂点番号
    V = 0
    for i in range(n):
        for j in range(n):
            if i<j:
                id[i][j] = V    # 0から順に各試合にidを割り振る
                V += 1
    def toID(i, j):     # 選手idから試合idを返す関数
        if i<j:         # i,jが逆になっても試合idは同じ
            return id[i][j]
        else:
            return id[j][i]
    
    to = [[] for _ in range(V)]     # 頂点間の辺の情報
    for i in range(n):
        for j in range(n-1):
            a[i][j] = toID(i, a[i][j])  # 選手idを試合id(頂点番号)に置き換える
        for j in range(n-2):        # 頂点間の依存関係はn-2個
            to[a[i][j+1]].append(a[i][j])

    dp, visited, calculated = [1] * V, [0] * V, [0] * V # Vからスタートしたときの最長経路。頂点の個数ベースで経路の長さを数えるので、初期値は1

    def dfs(v, dp, visited, calculated):
        if visited[v]:
            if not calculated[v]:   #  計算が終わっていない頂点を2度訪れるのはループがあるということ
                return -1
            return dp[v]
        visited[v] = 1
        for u in to[v]:     # 全ての辺をなめる
            res = dfs(u, dp, visited, calculated)
            if res == -1:   # ループがあれば-1を返す
                return -1
            dp[v] = max(dp[v], res+1)   # メモ化再帰っぽいこと(トポロジカルソートが同時にできる)
        calculated[v] = 1
        return dp[v]

    ans = 0
    for v in range(V):
        res = dfs(v, dp, visited, calculated)
        if res == -1:   # ループがあれば-1を返す（問題文の指示）
            print(-1)
            return
        ans = max(ans, res)
    print(ans)
    return

main()
