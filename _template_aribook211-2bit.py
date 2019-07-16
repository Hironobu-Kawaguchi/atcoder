# 蟻本をPythonで (初級編)
# https://qiita.com/saba/items/affc94740aff117d2ca9
# 例題 2-1-1 部分和問題

# 実はこの問題は再帰以外に bit で解くこともでき、以下のようになります。

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 0 から (2^n)-1 までループ
for bit in range(1 << n):
    sum = 0

    for i in range(n):
        # bit に i 番目のフラグが立っているかどうか
        if bit & (1 << i):
            # フラグが立っているならば sum に加算する
            sum += a[i]

    if sum == k:
        print("Yes")
        exit()

print("No")
