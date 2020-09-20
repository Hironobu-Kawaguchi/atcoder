# 蟻本をPythonで (初級編)
# https://qiita.com/saba/items/affc94740aff117d2ca9
# 2-2 猪突猛進！ "貪欲法"
# 例題 2-2-1　硬貨の問題
# 硬貨の問題

c = list(map(int, input().split()))
a = int(input())

# コインの金額
v = [1, 5, 10, 50, 100, 500]
ans = 0

for i in range(1, 7):
    t = min(a // v[-i], c[-i])  # コイン i を使う枚数
    a -= t * v[-i]
    ans += t

print(ans)