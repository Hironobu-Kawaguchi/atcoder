# B - バウムテスト
# https://atcoder.jp/contests/arc037/tasks/arc037_b

def dfs(now, prev):
    global flag
    # 今いる頂点から行ける頂点を順に next に入れてループ
    for next in g[now]:
        if next != prev:
            if memo[next]:
                # 過去に訪れていれば閉路
                flag = False
            else:
                memo[next] = True
                dfs(next, now)


n, m = map(int, input().split())
g = [[] * n for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

# 訪れたことがあるか
memo = [False for i in range(n)]

ans = 0
# 頂点をループ
for i in range(n):
    if not memo[i]:
        flag = True
        dfs(i, -1)
        if flag:
            # 閉路がなければ木である
            ans += 1
print(ans)