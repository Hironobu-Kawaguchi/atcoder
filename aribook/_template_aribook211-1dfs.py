# 蟻本をPythonで (初級編)
# https://qiita.com/saba/items/affc94740aff117d2ca9
# 例題 2-1-1 部分和問題

# i までで sum を作って、残り i 以降を調べる
def dfs(i, sum):
    # n 個決め終わったら、今までの和 sum が k と等しいかを返す
    if i == n:
        return sum == k

    # a[i] を使わない場合
    if dfs(i + 1, sum):
        return True

    # a[i] を使う場合
    if dfs(i + 1, sum + a[i]):
        return True

    # a[i] を使う使わないに拘らず k が作れないので False を返す
    return False


n, k = map(int, input().split())
a = list(map(int, input().split()))

if dfs(0, 0):
    print("Yes")
else:
    print("No")
